import os
import pytesseract
from PIL import Image
import pandas as pd
import re
from pathlib import Path
import logging
from datetime import datetime
import sys
import cv2
import numpy as np

# ------------------------------------------------------------------------------
# 1) If Tesseract is NOT in your PATH, explicitly set it here:
#    (Otherwise, you can comment this out if Tesseract is in PATH)
# ------------------------------------------------------------------------------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ------------------------------------------------------------------------------
# 2) Configure Logging
# ------------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='phone_extraction.log'
)

# ------------------------------------------------------------------------------
# 3) PhoneNumberExtractor Class
# ------------------------------------------------------------------------------
class PhoneNumberExtractor:
    def __init__(self, output_file):
        """
        Initialize the extractor with an output filename.
        We'll store phone data in a list of dictionaries, 
        then export to Excel at the end.
        """
        # script_dir is the folder where this script lives
        self.script_dir = Path(os.path.dirname(os.path.abspath(sys.argv[0])))
        self.output_file = self.script_dir / output_file
        self.phone_data = []

    def extract_phone_numbers(self, text):
        """
        Extract phone numbers from the recognized text.

        We use multiple patterns to catch different phone number formats 
        (e.g., India, US, raw +XXXXXXXX, etc.).
        """
        lines = text.split('\n')
        found_numbers = set()

        # Patterns for various phone number formats
        # Adjust these or add more as needed
        patterns = [
            r'\+\d{1,3}[\s-]?\d{5}[\s-]?\d{5}',    # Indian format e.g. +91 12345 67890
            r'\+\d{1,3}[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{4}',  # US/Canada e.g. +1 234-567-8901
            r'\+\d{1,3}[\s-]?\d{2,4}[\s-]?\d{3,4}[\s-]?\d{3,4}', # Other int'l combos
            r'\+\d{10,15}'  # Raw digits with plus, 10-15 length
        ]

        for line in lines:
            # Sometimes copy/paste can turn '+' into '＋'
            line = line.replace('＋', '+').strip()

            # Look for matches per pattern
            for pattern in patterns:
                matches = re.finditer(pattern, line)
                for match in matches:
                    number = match.group()
                    # Remove extra spaces, parentheses, or dashes
                    number = re.sub(r'[\s()-]', '', number)
                    # If it looks like a 10-digit number, assume Indian country code
                    if len(number) == 10 and number.isdigit():
                        number = '+91' + number
                    found_numbers.add(number)

        return list(found_numbers)

    def preprocess_image(self, image):
        """
        Specialized preprocessing for screenshot images using OpenCV.

        1) Convert to grayscale
        2) Increase contrast (CLAHE)
        3) Bilateral filter to reduce noise
        4) Adaptive threshold
        5) Scale up for better Tesseract recognition
        """
        # Convert Pillow image to np array
        img_np = np.array(image)

        # Convert to grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        # Increase contrast with CLAHE
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        contrast = clahe.apply(gray)

        # Bilateral filtering for noise reduction
        denoised = cv2.bilateralFilter(contrast, 9, 75, 75)

        # Adaptive thresholding
        thresh = cv2.adaptiveThreshold(
            denoised,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        # Scale up the image for better OCR accuracy
        height, width = thresh.shape
        scale_percent = 300  # e.g., triple the size
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        scaled = cv2.resize(thresh, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        return Image.fromarray(scaled)

    def process_image(self, image_path):
        """
        Process a single image file using Tesseract with multiple configs.

        1) Open the image with Pillow
        2) Preprocess using the specialized pipeline
        3) Run Tesseract with various page segmentation modes (PSM)
        4) Extract phone numbers from OCR text
        5) If nothing found, do a fallback method
        6) Store results in self.phone_data
        """
        try:
            with Image.open(image_path) as img:
                # Convert if not RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                processed_img = self.preprocess_image(img)

                # Multiple Tesseract configurations
                configs = [
                    '--oem 3 --psm 6 -c tessedit_char_whitelist=+0123456789()-\n ',
                    '--oem 3 --psm 4 -c tessedit_char_whitelist=+0123456789()-\n ',
                    '--oem 3 --psm 11 -c tessedit_char_whitelist=+0123456789()-\n '
                ]

                all_text = ""
                for config in configs:
                    text = pytesseract.image_to_string(processed_img, config=config)
                    all_text += "\n" + text

                # Extract phone numbers
                numbers = self.extract_phone_numbers(all_text)

                # If we found phone numbers, log them
                if numbers:
                    logging.info(f"Found {len(numbers)} phone numbers in {image_path.name}")
                    for number in numbers:
                        self.phone_data.append({
                            'Image': image_path.name,
                            'Phone Number': number,
                            'Extraction Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                else:
                    # Fallback approach: Try a simpler threshold
                    img_array = cv2.imread(str(image_path))
                    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
                    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                    text = pytesseract.image_to_string(binary, config='--oem 3 --psm 6')
                    numbers = self.extract_phone_numbers(text)

                    if numbers:
                        for number in numbers:
                            self.phone_data.append({
                                'Image': image_path.name,
                                'Phone Number': number,
                                'Extraction Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            })
                    else:
                        logging.warning(f"No phone numbers found in {image_path}")

        except Exception as e:
            logging.error(f"Error processing {image_path}: {str(e)}")
            print(f"Error processing {image_path}: {str(e)}")

    def process_directory(self):
        """
        Process all images in the script's directory.
        Looks for images with typical extensions and applies the process_image() method.
        """
        image_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')

        try:
            # Count how many images we have
            total_images = len([f for f in self.script_dir.glob('*') 
                                if f.suffix.lower() in image_extensions])
            processed = 0

            for image_path in self.script_dir.glob('*'):
                if image_path.suffix.lower() in image_extensions:
                    processed += 1
                    print(f"Processing image {processed}/{total_images}: {image_path.name}")
                    self.process_image(image_path)

            # After processing all images, save data if found
            if self.phone_data:
                df = pd.DataFrame(self.phone_data)
                # Remove duplicates
                df.drop_duplicates(inplace=True)
                df.to_excel(self.output_file, index=False)
                print(f"\nExtracted {len(df)} unique phone numbers")
                print(f"Results saved to {self.output_file}")
                logging.info(f"Results saved to {self.output_file}")
            else:
                print("\nNo phone numbers found in any images")
                logging.warning("No phone numbers found in any images")

        except Exception as e:
            logging.error(f"Error during directory processing: {str(e)}")
            print(f"Error during processing: {str(e)}")

# ------------------------------------------------------------------------------
# 4) main() Entry Point
# ------------------------------------------------------------------------------
def main():
    OUTPUT_FILE = "phone_numbers.xlsx"
    try:
        print("Phone Number Extractor")
        print("=====================")
        print("Looking for images in script directory...")

        extractor = PhoneNumberExtractor(OUTPUT_FILE)
        extractor.process_directory()

    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        print(f"\nAn error occurred: {str(e)}")
        print("Check the log file for details.")

if __name__ == "__main__":
    main()
