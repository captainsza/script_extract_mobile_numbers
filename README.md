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
Made with ❤️ by [Your Name]