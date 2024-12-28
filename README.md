# 📱 Phone Number Extractor

A powerful Python tool that extracts phone numbers from images using advanced OCR techniques. Perfect for bulk processing contact lists, screenshots, and business cards.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

## ✨ Features

- 🔍 Extracts phone numbers from multiple image formats (PNG, JPG, JPEG, TIFF, BMP)
- 🌏 Supports international phone number formats (India, US, Canada, and more)
- 📊 Exports results to Excel with timestamp tracking
- 🔄 Advanced image preprocessing for better accuracy
- 📝 Comprehensive logging system
- ⚡ Multi-threaded processing for better performance
- 🎯 High accuracy with multiple OCR passes

## 🚀 Quick Start

### Prerequisites

```bash
# Install required Python packages
pip install -r requirements.txt

# Install Tesseract OCR
# Windows: Download installer from https://github.com/UB-Mannheim/tesseract/wiki
# Linux: sudo apt install tesseract-ocr
# macOS: brew install tesseract
```

### Usage

1. Place your images in the same directory as the script
2. Run the script:
```bash
python script.py
```
3. Find results in `phone_numbers.xlsx`

## 📋 Requirements

- Python 3.6+
- Tesseract OCR
- Required Python packages:
  - pytesseract
  - Pillow
  - pandas
  - opencv-python
  - numpy
  - openpyxl

## 🛠️ Configuration

The script is highly configurable. Key settings can be found at the top of the script:

```python
# Tesseract path (if not in system PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Supported image extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp')

# Output filename
OUTPUT_FILE = "phone_numbers.xlsx"
```

## 📊 Output Format

The script generates an Excel file with the following columns:
- Image: Source image filename
- Phone Number: Extracted phone number
- Extraction Date: Timestamp of extraction

## 🎯 Supported Phone Number Formats

- Indian format: +91 XXXXX XXXXX
- US/Canada format: +1 XXX-XXX-XXXX
- International format: +[country code] XXXXXXXXXX
- Raw number format: +XXXXXXXXXXXX

## 🔍 How It Works

1. **Image Preprocessing**
   - Grayscale conversion
   - Contrast enhancement (CLAHE)
   - Noise reduction
   - Adaptive thresholding
   - Image scaling

2. **OCR Processing**
   - Multiple Tesseract configurations
   - Different page segmentation modes
   - Fallback processing for difficult images

3. **Number Extraction**
   - Regular expression pattern matching
   - Format validation
   - Duplicate removal
   - Country code normalization

## 📝 Logging

The script maintains detailed logs in `phone_extraction.log`, tracking:
- Processing start/end times
- Numbers found per image
- Errors and warnings
- Overall statistics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for the OCR engine
- [OpenCV](https://opencv.org/) for image processing
- [Pandas](https://pandas.pydata.org/) for data handling

## 📞 Contact

If you have any questions or suggestions, please feel free to reach out or create an issue.

---
Made with ❤️ by Zaid Ahmad

## 📝 Exmple
```bash
C:\Users\pc\personal project\script drive numbers>python script.py
Phone Number Extractor
=====================
Looking for images in script directory...
Processing image 1/99: 1.jpeg
Processing image 2/99: 10.jpeg
Processing image 3/99: 11.jpeg
Processing image 4/99: 12.jpeg
Processing image 5/99: 13.jpeg
Processing image 6/99: 14.jpeg
Processing image 7/99: 2.jpeg
Processing image 8/99: 3.jpeg
Processing image 9/99: 4.jpeg
Processing image 10/99: 5.jpeg
Processing image 11/99: 6.jpeg
Processing image 12/99: 7.jpeg
Processing image 13/99: 8.jpeg
Processing image 14/99: 9.jpeg
Processing image 15/99: gg.jpeg
Processing image 16/99: Screenshot_2024-12-28-11-57-14-26_7352322957d4404136654ef4adb64504.jpg
Processing image 17/99: Screenshot_2024-12-28-11-57-20-59_7352322957d4404136654ef4adb64504.jpg
Processing image 18/99: Screenshot_2024-12-28-11-57-33-30_7352322957d4404136654ef4adb64504.jpg
Processing image 19/99: Screenshot_2024-12-28-11-57-42-37_7352322957d4404136654ef4adb64504.jpg
Processing image 20/99: Screenshot_2024-12-28-11-57-49-50_7352322957d4404136654ef4adb64504.jpg
Processing image 21/99: Screenshot_2024-12-28-11-57-54-48_7352322957d4404136654ef4adb64504.jpg
Processing image 22/99: Screenshot_2024-12-28-11-58-01-27_7352322957d4404136654ef4adb64504.jpg
Processing image 23/99: Screenshot_2024-12-28-11-58-06-86_7352322957d4404136654ef4adb64504.jpg
Processing image 24/99: Screenshot_2024-12-28-11-58-11-98_7352322957d4404136654ef4adb64504.jpg
Processing image 25/99: Screenshot_2024-12-28-11-58-18-51_7352322957d4404136654ef4adb64504.jpg
Processing image 26/99: Screenshot_2024-12-28-11-58-23-74_7352322957d4404136654ef4adb64504.jpg
Processing image 27/99: Screenshot_2024-12-28-11-58-30-13_7352322957d4404136654ef4adb64504.jpg
Processing image 28/99: Screenshot_2024-12-28-11-59-15-58_7352322957d4404136654ef4adb64504.jpg
Processing image 29/99: Screenshot_2024-12-28-11-59-22-46_7352322957d4404136654ef4adb64504.jpg
Processing image 30/99: Screenshot_2024-12-28-11-59-29-78_7352322957d4404136654ef4adb64504.jpg
Processing image 31/99: Screenshot_2024-12-28-12-00-00-25_7352322957d4404136654ef4adb64504.jpg
Processing image 32/99: Screenshot_2024-12-28-12-00-10-47_7352322957d4404136654ef4adb64504.jpg
Processing image 33/99: Screenshot_2024-12-28-12-00-18-52_7352322957d4404136654ef4adb64504.jpg
Processing image 34/99: Screenshot_2024-12-28-12-00-23-50_7352322957d4404136654ef4adb64504.jpg
Processing image 35/99: Screenshot_2024-12-28-12-00-28-39_7352322957d4404136654ef4adb64504.jpg
Processing image 36/99: Screenshot_2024-12-28-12-00-34-68_7352322957d4404136654ef4adb64504.jpg
Processing image 37/99: Screenshot_2024-12-28-12-00-44-64_7352322957d4404136654ef4adb64504.jpg
Processing image 38/99: Screenshot_2024-12-28-12-00-49-99_7352322957d4404136654ef4adb64504.jpg
Processing image 39/99: Screenshot_2024-12-28-12-00-56-20_7352322957d4404136654ef4adb64504.jpg
Processing image 40/99: Screenshot_2024-12-28-12-01-02-95_7352322957d4404136654ef4adb64504.jpg
Processing image 41/99: Screenshot_2024-12-28-12-01-08-51_7352322957d4404136654ef4adb64504.jpg
Processing image 42/99: Screenshot_2024-12-28-12-01-15-38_7352322957d4404136654ef4adb64504.jpg
Processing image 43/99: Screenshot_2024-12-28-12-01-22-41_7352322957d4404136654ef4adb64504.jpg
Processing image 44/99: Screenshot_2024-12-28-12-01-32-24_7352322957d4404136654ef4adb64504.jpg
Processing image 45/99: Screenshot_2024-12-28-12-01-39-45_7352322957d4404136654ef4adb64504.jpg
Processing image 46/99: Screenshot_2024-12-28-12-01-48-65_7352322957d4404136654ef4adb64504.jpg
Processing image 47/99: Screenshot_2024-12-28-12-01-57-02_7352322957d4404136654ef4adb64504.jpg
Processing image 48/99: Screenshot_2024-12-28-12-02-05-04_7352322957d4404136654ef4adb64504.jpg
Processing image 49/99: Screenshot_2024-12-28-12-02-11-82_7352322957d4404136654ef4adb64504.jpg
Processing image 50/99: Screenshot_2024-12-28-12-02-19-17_7352322957d4404136654ef4adb64504.jpg
Processing image 51/99: Screenshot_2024-12-28-12-02-25-98_7352322957d4404136654ef4adb64504.jpg
Processing image 52/99: Screenshot_2024-12-28-12-02-34-00_7352322957d4404136654ef4adb64504.jpg
Processing image 53/99: Screenshot_2024-12-28-12-02-40-62_7352322957d4404136654ef4adb64504.jpg
Processing image 54/99: Screenshot_2024-12-28-12-02-48-90_7352322957d4404136654ef4adb64504.jpg
Processing image 55/99: Screenshot_2024-12-28-12-02-56-63_7352322957d4404136654ef4adb64504.jpg
Processing image 56/99: Screenshot_2024-12-28-12-03-06-15_7352322957d4404136654ef4adb64504.jpg
Processing image 57/99: Screenshot_2024-12-28-12-03-19-31_7352322957d4404136654ef4adb64504.jpg
Processing image 58/99: Screenshot_2024-12-28-12-03-26-09_7352322957d4404136654ef4adb64504.jpg
Processing image 59/99: Screenshot_2024-12-28-12-03-34-85_7352322957d4404136654ef4adb64504.jpg
Processing image 60/99: Screenshot_2024-12-28-12-03-42-25_7352322957d4404136654ef4adb64504.jpg
Processing image 61/99: Screenshot_2024-12-28-12-03-48-42_7352322957d4404136654ef4adb64504.jpg
Processing image 62/99: Screenshot_2024-12-28-12-03-57-95_7352322957d4404136654ef4adb64504.jpg
Processing image 63/99: Screenshot_2024-12-28-12-04-04-26_7352322957d4404136654ef4adb64504.jpg
Processing image 64/99: Screenshot_2024-12-28-12-04-14-77_7352322957d4404136654ef4adb64504.jpg
Processing image 65/99: Screenshot_2024-12-28-12-04-25-63_7352322957d4404136654ef4adb64504.jpg
Processing image 66/99: Screenshot_2024-12-28-12-04-32-67_7352322957d4404136654ef4adb64504.jpg
Processing image 67/99: Screenshot_2024-12-28-12-04-40-06_7352322957d4404136654ef4adb64504.jpg
Processing image 68/99: Screenshot_2024-12-28-12-04-47-71_7352322957d4404136654ef4adb64504.jpg
Processing image 69/99: Screenshot_2024-12-28-12-04-55-92_7352322957d4404136654ef4adb64504.jpg
Processing image 70/99: Screenshot_2024-12-28-12-05-03-11_7352322957d4404136654ef4adb64504.jpg
Processing image 71/99: Screenshot_2024-12-28-12-05-12-30_7352322957d4404136654ef4adb64504.jpg
Processing image 72/99: Screenshot_2024-12-28-12-05-22-08_7352322957d4404136654ef4adb64504.jpg
Processing image 73/99: Screenshot_2024-12-28-12-05-29-18_7352322957d4404136654ef4adb64504.jpg
Processing image 74/99: Screenshot_2024-12-28-12-05-35-91_7352322957d4404136654ef4adb64504.jpg
Processing image 75/99: Screenshot_2024-12-28-12-05-42-27_7352322957d4404136654ef4adb64504.jpg
Processing image 76/99: Screenshot_2024-12-28-12-05-53-78_7352322957d4404136654ef4adb64504.jpg
Processing image 77/99: Screenshot_2024-12-28-12-06-00-89_7352322957d4404136654ef4adb64504.jpg
Processing image 78/99: Screenshot_2024-12-28-12-06-13-15_7352322957d4404136654ef4adb64504.jpg
Processing image 79/99: Screenshot_2024-12-28-12-06-22-82_7352322957d4404136654ef4adb64504.jpg
Processing image 80/99: Screenshot_2024-12-28-12-06-32-71_7352322957d4404136654ef4adb64504.jpg
Processing image 81/99: Screenshot_2024-12-28-12-06-39-48_7352322957d4404136654ef4adb64504.jpg
Processing image 82/99: Screenshot_2024-12-28-12-06-46-86_7352322957d4404136654ef4adb64504.jpg
Processing image 83/99: Screenshot_2024-12-28-12-07-00-77_7352322957d4404136654ef4adb64504.jpg
Processing image 84/99: Screenshot_2024-12-28-12-07-11-81_7352322957d4404136654ef4adb64504.jpg
Processing image 85/99: Screenshot_2024-12-28-12-07-17-88_7352322957d4404136654ef4adb64504.jpg
Processing image 86/99: Screenshot_2024-12-28-12-07-25-36_7352322957d4404136654ef4adb64504.jpg
Processing image 87/99: Screenshot_2024-12-28-12-07-35-03_7352322957d4404136654ef4adb64504.jpg
Processing image 88/99: Screenshot_2024-12-28-12-07-43-11_7352322957d4404136654ef4adb64504.jpg
Processing image 89/99: Screenshot_2024-12-28-12-07-50-15_7352322957d4404136654ef4adb64504.jpg
Processing image 90/99: Screenshot_2024-12-28-12-07-57-82_7352322957d4404136654ef4adb64504.jpg
Processing image 91/99: Screenshot_2024-12-28-12-08-04-51_7352322957d4404136654ef4adb64504.jpg
Processing image 92/99: Screenshot_2024-12-28-12-08-11-84_7352322957d4404136654ef4adb64504.jpg
Processing image 93/99: Screenshot_2024-12-28-12-08-18-25_7352322957d4404136654ef4adb64504.jpg
Processing image 94/99: Screenshot_2024-12-28-12-08-25-32_7352322957d4404136654ef4adb64504.jpg
Processing image 95/99: Screenshot_2024-12-28-12-08-32-12_7352322957d4404136654ef4adb64504.jpg
Processing image 96/99: Screenshot_2024-12-28-12-08-45-09_7352322957d4404136654ef4adb64504.jpg
Processing image 97/99: Screenshot_2024-12-28-12-08-50-37_7352322957d4404136654ef4adb64504.jpg
Processing image 98/99: Screenshot_2024-12-28-12-09-02-24_7352322957d4404136654ef4adb64504.jpg
Processing image 99/99: Screenshot_2024-12-28-12-09-26-56.jpg

Extracted 1853 unique phone numbers
Results saved to C:\Users\pc\personal project\script drive numbers\phone_numbers.xlsx
```