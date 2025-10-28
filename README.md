# PDF to Audiobook Converter

A simple web application built with Flask that converts PDF files into audiobooks using text-to-speech (TTS). Upload a PDF, select a voice, and download the generated MP3 audiobook.

## Features
- **PDF Text Extraction**: Extracts text from uploaded PDF files using `pdfplumber`.
- **Text-to-Speech Conversion**: Generates audio using `pyttsx3` in a subprocess to avoid threading issues.
- **Voice Selection**: Choose from default, male, or female voices.
- **Web Interface**: Clean, responsive UI built with Bootstrap.
- **Error Handling**: Displays user-friendly messages for common issues (e.g., no text in PDF, generation failures).
- **File Management**: Automatically cleans up temporary files.

## Prerequisites
- Python 3.8 or higher.
- Internet connection (if using alternative TTS libraries in the future).
- Basic knowledge of running Python scripts.

## Installation
1. Clone or download this repository:
