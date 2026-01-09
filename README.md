# Spam & Scam Detection System

A Machine Learning–based system that detects **spam messages, phishing emails, and potential job scams** using Natural Language Processing (NLP).  
The application provides a simple user interface to check whether a message is **Spam**, **Not Spam**, or **Potential Scam**.

---

## Features

- Detects **spam messages** (promotions, ads, marketing spam)
- Detects **phishing emails** (bank, login, password, suspicious links)
- Flags **job/internship scam messages** as *Potential Scam*
- Uses **Machine Learning + Rule-based hybrid approach**
- Simple and clean **Flask-based UI**
- Real-time prediction with confidence score

---

## Technologies Used

- **Python**
- **Flask** (for application interface)
- **Scikit-learn**
- **NLTK** (Natural Language Processing)
- **HTML, CSS, JavaScript**
- **Git & GitHub**

---

## Machine Learning Details

- Text preprocessing using:
  - Lowercasing
  - Stopword removal
  - Stemming
- Feature extraction using **TF-IDF Vectorizer**
- Classification using **Machine Learning model**
- Additional **rule-based detection** for phishing and job scams

---

## Project Structure
Spam_Email_Detection/
│
├── app.py # Flask application
├── train_model.py # Model training script
├── model/
│ ├── spam_model.pkl
│ └── vectorizer.pkl
├── templates/
│ └── index.html
├── static/
│ ├── style.css
│ └── script.js
└── README.md

