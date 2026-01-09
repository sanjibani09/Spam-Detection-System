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

## How It Works

1. The user enters a message or email text in the interface.
2. The text is cleaned using NLP techniques such as lowercasing, stopword removal, and stemming.
3. TF-IDF is used to convert text into numerical features.
4. A trained Machine Learning model predicts whether the message is Spam or Not Spam.
5. Additional rule-based checks flag phishing and job-related scam messages as Potential Scam.
6. The result is displayed instantly to the user.


##  Use Cases
- Checking suspicious emails or messages
- Identifying phishing attempts
- Detecting fake job or internship offers
- Helping students avoid online scams
- Educational use for learning NLP and ML


##  Model Logic
- Spam classification is performed using a Machine Learning model trained on labeled data.
- Phishing messages are detected using keyword and pattern-based rules.
- Job and internship scams are flagged based on risk indicators such as urgency and requests for personal information.
- This hybrid approach improves reliability and reduces false positives.

