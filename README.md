# 📧 Email Classification System with PII Masking

This project implements a FastAPI-based email classification system that:
- Masks personally identifiable information (PII) in emails using regular expressions.
- Classifies emails into categories such as `Incident`, `Request`, `Change`, and `Problem`.
- Provides a REST API endpoint `/classify` for email processing and classification.

---

## 🚀 Features

- Regex-based PII masking (no LLMs used)
- Email classification using TF-IDF vectorizer and Naive Bayes classifier
- FastAPI backend with a POST `/classify` endpoint
- Deployment-ready on Hugging Face Spaces or any compatible platform

---

## 📁 Project Structure

```

project-root/
├── app.py                  # FastAPI application
├── classifier.py           # Model training and prediction logic
├── pii\_masker.py           # PII masking using regex
├── requirements.txt        # Python dependencies
├── model.pkl               # Serialized trained model (generated after training)
├── combined\_emails\_with\_natural\_pii.csv  # Training dataset (not included)
├── README.md               # This documentation file

````

---

## 🛠️ Installation

Clone the repo and install dependencies:

```bash
git clone <repo_url>
cd <repo_directory>
pip install -r requirements.txt
````

---

## 📦 Running the API Locally

Start the FastAPI app with:

```bash
uvicorn app:app --reload
```

---

## 🧪 API Usage

### POST `/classify`

**Request Body:**

```json
{
  "input_email_body": "Hello, my name is John Doe and my email is johndoe@gmail.com"
}
```

**Response Example:**

```json
{
  "input_email_body": "Hello, my name is John Doe and my email is johndoe@gmail.com",
  "list_of_masked_entities": [
    {
      "position": [18, 26],
      "classification": "full_name",
      "entity": "John Doe"
    },
    {
      "position": [45, 63],
      "classification": "email",
      "entity": "johndoe@gmail.com"
    }
  ],
  "masked_email": "Hello, my name is [full_name] and my email is [email]",
  "category_of_the_email": "Request"
}
```

---

## ☁️ Deployment on Hugging Face Spaces

1. Create a new Space with SDK set to **docker** or **FastAPI**.
2. Upload all project files to the Space root.
3. Ensure your `.huggingface.yml` and `Dockerfile` (if using docker) are correctly configured.
4. Access the POST `/classify` endpoint to test.

---

## 📋 Assignment Requirements Covered

* PII masking with regex patterns
* Email classification using Naive Bayes and TF-IDF
* FastAPI app exposing a `/classify` POST endpoint
* JSON input/output format compliance
* Deployment readiness and reproducibility

---
