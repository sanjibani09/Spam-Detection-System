import pandas as pd
import re
df = pd.read_csv("data/spam.csv", encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'message']
print("Dataset loaded successfully")
print(df.head())
print("\nSpam vs Ham count:")
print(df['label'].value_counts())
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
ps = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', ' emailaddress ', text)
    text = re.sub(r'http\S+|www\S+', ' webaddress ', text)
    text = re.sub(r'\d+', ' number ', text)
    text = ''.join(ch for ch in text if ch not in string.punctuation)
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stopwords.words('english')]
    return " ".join(words)
df['clean_message'] = df['message'].apply(clean_text)

print("\nCleaned text sample:")
print(df[['message', 'clean_message']].head())
from sklearn.feature_extraction.text import TfidfVectorizer


tfidf = TfidfVectorizer(
    max_features=6000,
    ngram_range=(1, 2)
)
X = tfidf.fit_transform(df['clean_message']).toarray()

y = df['label'].map({'ham': 0, 'spam': 1})

print("\nTF-IDF feature shape:", X.shape)
print("Labels shape:", y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training samples:", X_train.shape)
print("Testing samples:", X_test.shape)
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
import pickle

pickle.dump(model, open("model/spam_model.pkl", "wb"))
pickle.dump(tfidf, open("model/vectorizer.pkl", "wb"))

print("Model retrained and saved successfully")

