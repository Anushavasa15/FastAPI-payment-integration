
from fastapi import FastAPI, HTTPException , Request
from pydantic import BaseModel
import stripe
from fastapi.responses import HTMLResponse
import os

app = FastAPI()


stripe.api_key = "sk_test_51Pgl742LeFdiFZkFMyrWIaGKxQ4g7grVbPBcX0PenS5LFRWkNCTblXuyY3AwduxEk6He97MouA4aYsnMjYQ3m8Db00nRhKwEOj"

#stripe.api_key = os.getenv("STRIPE_API_KEY")

class CreatePaymentRequest(BaseModel):
    number: str
    exp_month: int
    exp_year: int
    cvc: str


@app.post("/payments/create")
async def create_payment(request: CreatePaymentRequest):
    try:
        
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={
                "number": request.number,
                "exp_month": request.exp_month,
                "exp_year": request.exp_year,
                "cvc": request.cvc,
            },
        )
        return payment_method
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))





@app.get("/payments/{payment_id}")
async def retrieve_payment_method(payment_id: str):
    try:
        
        payment_method = stripe.PaymentMethod.retrieve(payment_id)
        return payment_method
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.post("/create-webhook-endpoint")
async def create_webhook_endpoint():
    try:
        webhook_endpoint = stripe.WebhookEndpoint.create(
            enabled_events=["charge.succeeded", "charge.failed"],
            url="https://example.com/my/webhook/endpoint",
        )
        return {"webhook_endpoint": webhook_endpoint}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/")
async def get_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())


