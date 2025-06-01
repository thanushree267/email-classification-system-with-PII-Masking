import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Trains and saves the model using TF-IDF + Naive Bayes
def train_model(data_path='combined_emails_with_natural_pii.csv'):
    df = pd.read_csv(data_path)
    X = df['email']  # Input emails
    y = df['type']   # Email categories

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vec, y)

    # Save both model and vectorizer to a pickle file
    with open("model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
    print("✅ Model trained and saved to model.pkl")

# Predict the category of a given email
def predict(text):
    with open("model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)
    X_vec = vectorizer.transform([text])
    return model.predict(X_vec)[0]
