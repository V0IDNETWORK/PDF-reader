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
