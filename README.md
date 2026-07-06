# AI Smart Language Translator

## Project Overview

AI Smart Language Translator is a Python-based web application that translates text between multiple languages using AI-powered translation services. The application provides an interactive interface where users can input text, select languages, and receive translated output instantly.

The project also includes additional intelligent features such as voice input, text-to-speech, language detection, translation history, and a modern user interface.

---

## Features

✓ Multi-language text translation

✓ Automatic language detection

✓ Voice input (Speech-to-Text)

✓ Text-to-Speech output

✓ Copy translated text

✓ Dark mode

✓ Swap source and target languages

✓ Translation history using SQLite database

✓ Responsive user interface

✓ Real-time translation

---

## Technologies Used

Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask

Database:
- SQLite

Libraries:
- Flask
- Flask-SQLAlchemy
- deep-translator
- gTTS
- langdetect

---

## Project Structure

AI_Smart_Translator/

├── app.py

├── requirements.txt

├── translator.db

│

├── templates/

│   └── index.html

│

├── static/

│   ├── style.css

│   ├── script.js

│   └── output.mp3

---

## Installation

Step 1: Clone project

git clone <repository_link>

Move into project folder:

cd AI_Smart_Translator

---

Step 2: Install required packages

pip install -r requirements.txt

or manually install:

pip install flask

pip install flask-sqlalchemy

pip install deep-translator

pip install gtts

pip install langdetect

---

## Running Project

Run the Flask application:

python app.py

Open browser:

http://127.0.0.1:5000

---

## How to Use

1. Enter text in input area

2. Select source language

3. Select target language

4. Click Translate button

5. View translated result

6. Use additional features:

- Click Copy button to copy text
- Click Listen button for speech output
- Click Speak button for voice input
- Click Dark Mode to change theme
- Click History to see previous translations

---

## Workflow

User Input

↓

Language Selection

↓

Translation API Processing

↓

Translated Output

↓

Store Translation History

↓

Optional Speech Output

---

## Future Enhancements

- PDF document translation

- Image OCR translation

- User authentication system

- Analytics dashboard

- AI grammar correction

- Chat-based translator

- Translation export as PDF

- Favorite translations

---

## Screenshots

<img width="1366" height="768" alt="Screenshot 2026-07-06 125500" src="https://github.com/user-attachments/assets/e097f7f8-5566-4cab-b573-1798999d808e" />

Example:

Home Screen

Translation Output

Dark Mode Interface

History Page

---

## Author

Name: Tanisha Mittal

Project: AI Smart Language Translator

Technology: Python + Flask + AI Translation

---

## License

This project is open-source and free for educational purposes.
