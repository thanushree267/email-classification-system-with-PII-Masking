from fastapi import FastAPI
from pydantic import BaseModel
from pii_masker import mask_pii
from classifier import predict

app = FastAPI()

class EmailInput(BaseModel):
    input_email_body: str

@app.post("/classify")
def classify_email(email: EmailInput):
    original_email = email.input_email_body
    masked_email, entities = mask_pii(original_email)
    category = predict(masked_email)

    return {
        "input_email_body": original_email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
