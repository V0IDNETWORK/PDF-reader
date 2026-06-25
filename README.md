# 🚀 PDF-READER

**Author:** `MR. Nothing`  
**License:** MIT  
**Language:** Python  
**Version:** 1.0.0  
**Project Type:** OCR (Optical Character Recognition) Toolkit  

---

# 📖 Introduction

NIP-READER is a **cutting-edge OCR (Optical Character Recognition) toolkit** designed to extract text from multiple sources including **PDF documents, images (JPG, PNG, BMP), and Microsoft Word files (DOCX)**.  
It is built with a strong foundation in **Python, OpenCV, Tesseract OCR, and modern libraries** to provide a **fast, reliable, and professional solution** for text recognition tasks.

OCR technology is critical in today’s world where vast amounts of information are locked inside scanned documents, photos, or research papers.  
With NIP-READER, you can easily **digitize, analyze, and repurpose text-based data** from any supported file type.

This project was created and is maintained by **@niproot** as part of a broader vision to develop professional-grade open-source tools for document processing and cybersecurity research.

---

# ✨ Key Features

✅ **PDF to Text Conversion** – Converts high-quality PDFs (scanned or digital) into readable and searchable text.  
✅ **Image to Text (OCR)** – Extracts text from JPG, PNG, BMP images using advanced preprocessing.  
✅ **Word to Text Conversion** – Reads DOCX documents and saves extracted text in `.txt` format.  
✅ **Smart Image Preprocessing** – Uses **Thresholding & Adaptive Thresholding** to enhance recognition accuracy.  
✅ **Auto File Type Detection** – Automatically detects whether the input is PDF, image, or Word file.  
✅ **Multi-language Support** – Works with any Tesseract OCR-supported language (English, Persian, German, etc.).  
✅ **CLI with Style** – A professional command-line interface with colored outputs, ASCII banners, and interactive input.  
✅ **Cross-Platform** – Supports Linux, Windows, and macOS with adaptive installation scripts.  
✅ **Installer Script** – Automated installation of Python dependencies and OCR languages.  
✅ **Error Handling & Logging** – Provides detailed error messages for debugging and improved stability.  

---

# 🛠️ Technology Stack

- **Python 3.10+**
- **OpenCV (cv2)** – For image processing & preprocessing.  
- **Tesseract OCR (pytesseract)** – For text recognition.  
- **pdf2image** – Converts PDFs into high-resolution images for OCR.  
- **Colorama** – Adds styled and colored outputs for CLI.  
- **PyFiglet** – Renders ASCII banners.  
- **NumPy** – Efficient array manipulation for images.  
- **python-docx** – Reads Microsoft Word files.  

---

# 📦 Installation Guide

## 1️⃣ Clone Repository
```bash
git clone https://github.com/niproot/NIP-READER.git
cd NIP-READER
```

## 2️⃣ Install Dependencies
Run the installer script:
```bash
python3 installer.py
```

### Linux (Debian/Ubuntu)
The installer will auto-detect and run:
```bash
sudo apt update
sudo apt install python3-pip tesseract-ocr -y
pip install -r requirements.txt
```

### Linux (Arch)
```bash
sudo pacman -Syu
sudo pacman -S python-pip tesseract tesseract-data-eng
```

### Windows
- Install Python manually from [python.org](https://www.python.org/downloads/).
- Install [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki).  
- Then run:  
```bash
pip install -r requirements.txt
```

## 3️⃣ Run the Application
```bash
python3 main.py
```

---

# 🖥️ CLI Preview

When you launch the program, you’ll see a stylish interface:

```
 _   _ ___ ____       ____  _____    _    ____  _____ ____  
| \ | |_ _|  _ \     |  _ \| ____|  / \  |  _ \| ____|  _ \ 
|  \| || || |_) |____| |_) |  _|   / _ \ | | | |  _| | |_) |
| |\  || ||  __/_____|  _ <| |___ / ___ \| |_| | |___|  _ < 
|_| \_|___|_|        |_| \_\_____/_/   \_\____/|_____|_| \_```

Options:
```
1. PDF -> Text
2. Image -> Text
3. Word -> Text
4. Exit
```

---

# ⚙️ How It Works (Step-by-Step)

1. **User Input** – The user selects a file (PDF, image, or DOCX).  
2. **File Detection** – The system auto-detects the file type.  
3. **Preprocessing** –  
   - Converts the file into an image (if PDF or DOCX).  
   - Converts image to grayscale.  
   - Applies **Thresholding** or **Adaptive Thresholding** depending on image variance.  
4. **OCR Execution** – Tesseract extracts the text using the specified language.  
5. **Save Results** – Output is stored in a timestamped `.txt` file.  
6. **User Feedback** – CLI informs the user with styled logs and messages.  

---

# 📂 Project Structure

```
📦 NIP-READER
 ┣ 📜 installer.py   # Installer for dependencies & OCR languages
 ┣ 📜 main.py        # Core OCR logic & CLI interface
 ┣ 📜 README.md      # Full project documentation
 ┣ 📜 LICENSE        # MIT License file
 ┗ 📜 DOCUMENT.md    # Technical documentation (developer notes)
```

---

# 🔬 Modules Overview

## 1️⃣ installer.py
- Detects operating system.  
- Installs required Python libraries.  
- Installs Tesseract OCR and additional languages.  
- Verifies that essential project files exist.  

## 2️⃣ main.py
- Core OCR logic.  
- Functions for **PDF to Text, Image to Text, Word to Text**.  
- CLI with options for user interaction.  
- Uses asynchronous functions (`asyncio`) for non-blocking processing.  
- Image preprocessing pipeline for accuracy boost.  

---

# 📊 Example Workflows

### Example 1: PDF to Text
```bash
python3 main.py
# Select option 1
# Enter: sample.pdf
```
Output: `res_pdf_20250911_200528.txt`

### Example 2: Image to Text
```bash
python3 main.py
# Select option 2
# Enter: receipt.png
```
Output: `res_image_20250911_201234.txt`

### Example 3: Word to Text
```bash
python3 main.py
# Select option 3
# Enter: report.docx
```
Output: `res_docx_20250911_202345.txt`

---

# 🌍 Multi-Language OCR

You can install multiple OCR languages such as:
- English (`en`)
- Persian (`fa`)
- German (`de`)
- Arabic (`ar`)
- French (`fr`)  

### Example:
```bash
Enter PDF Path: document.pdf
Enter OCR language: fa
```

---

# 📈 Performance Notes

- Preprocessing with **Adaptive Thresholding** significantly improves OCR results on noisy images.  
- Higher DPI improves text recognition. Recommended: **300–400 DPI**.  
- Multi-threaded processing can be added in future updates for faster OCR on large PDFs.  

---

# 🧩 Future Roadmap

- GUI Interface (PyQt / Tkinter).  
- GPU acceleration with CUDA-enabled OpenCV.  
- Support for more file formats (TXT, XLSX, PPTX).  
- Machine learning integration for **intelligent document recognition**.  
- Export results to structured formats (JSON, CSV).  

---

# 🤝 Contributing

We welcome contributions from the open-source community!  
To contribute:  
1. Fork the repository.  
2. Create a feature branch.  
3. Commit your changes.  
4. Open a Pull Request.  

Please ensure your code follows **PEP8 style guidelines** and includes comments.  

---

# 🧑‍💻 Author

**👤 Maintainer:** [@niproot](https://github.com/niproot)  
- 💻 Python Developer  
- 🕵️ Cybersecurity Enthusiast  
- 📖 Open Source Contributor  

---

# 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---
# 📘 Technical Documentation - NIP-READER

## 🔹 Overview
**NIP-READER** is a Python-based OCR tool designed to extract text from **PDFs, Images, and Word files**.  
It leverages **Tesseract OCR**, **OpenCV**, and **Python libraries** to deliver accurate and efficient text recognition.

---

## 🔹 Modules

### 1️⃣ installer.py
- Detects operating system (Windows/Linux/Arch/Debian)
- Installs required Python packages
- Installs OCR languages (e.g., `en`, `fa`, `de`)
- Verifies the existence of essential project files

### 2️⃣ main.py
- Provides **image preprocessing** (Threshold & Adaptive Threshold)
- Converts **PDFs to text**
- Extracts **text from images**
- Reads **Word (DOCX) files**
- Implements a **user-friendly CLI** with PyFiglet & Colorama

---

## 🔹 Dependencies
- `pytesseract`
- `pdf2image`
- `opencv-python`
- `colorama`
- `pyfiglet`
- `numpy`
- `python-docx`

---

## 🔹 Workflow
1. User selects the input file.
2. Program automatically detects the file type (PDF, Image, DOCX).
3. Image is preprocessed (Grayscale + Threshold).
4. Tesseract OCR extracts the text.
5. Extracted text is saved into an output `.txt` file.

---

## 🔹 Future Roadmap
- Support for more formats (TXT, PPTX, XLSX)
- Graphical User Interface (GUI)
- GPU-accelerated OCR for faster processing
- AI-powered models for improved accuracy

---

## 🔹 Example Use Cases
- Digitizing scanned books & documents
- Extracting text from research papers
- Converting handwritten notes into digital text (with Tesseract training)
- Automating data extraction workflows

# 🎯 Final Notes

NIP-READER is designed with **professionalism, extensibility, and usability** in mind.  
It bridges the gap between **raw OCR libraries** and a **user-friendly toolkit**, providing a **powerful solution for developers, researchers, and everyday users**.

If you find this project useful, consider giving it a ⭐ on GitHub and sharing it with others!

---
