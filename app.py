from flask import Flask, render_template, request, jsonify
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
app = Flask(__name__, template_folder="templates", static_folder="static")
model = pickle.load(open("model/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
ps = PorterStemmer()
def clean_text(text):
    text = text.lower()
    text = ''.join(ch for ch in text if ch not in string.punctuation)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    return " ".join(words)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["email"]
    cleaned = clean_text(data)
    vector = vectorizer.transform([cleaned]).toarray()
    spam_prob = model.predict_proba(vector)[0][1]
    phishing_keywords = [
        "verify", "login", "account", "bank",
        "suspend", "suspended", "password",
        "confirm", "urgent", "click"
    ]
    rule_flag = (
        any(word in data.lower() for word in phishing_keywords)
        and ("http" in data.lower() or "@" in data)
    )
    job_scam_keywords = [
        "work from home", "earn", "part time", "full time",
        "income", "age requirement", "drop your details",
        "contact number", "whatsapp", "online opportunity"
    ]

    text_lower = data.lower()
    job_scam_flag = any(word in text_lower for word in job_scam_keywords)
    sensitive_info_keywords=["id proof", "aadhar", "pan", "resume",
    "documents", "onboarding", "verification",
    "send your", "submit your"]
    sensitive_flag = any(word in data.lower() for word in sensitive_info_keywords)

    if spam_prob > 0.4 or rule_flag:
        result = "Spam"
    elif job_scam_flag or sensitive_flag:
        result ="Potential Scam"
    else:
        result = "Not Spam"

    return jsonify({
        "result": result,
        "confidence": round(spam_prob * 100, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
