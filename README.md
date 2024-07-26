API Endpoints
Create Payment
Endpoint: /payments/create

Method: POST

Request Body: 
      {
  "number": "4242424242424242",
  "exp_month": 8,
  "exp_year": 2026,
  "cvc": "314"
}

Response: Payment method details or error message.



Retrieve Payment Method :

 Endpoint: /payments/{payment_id}

Method: GET

URL Parameter: payment_id (ID of the payment method)
Response: Payment method details or error message.




Create Webhook Endpoint:

Endpoint: /create-webhook-endpoint
Method: POST
Response: Webhook endpoint details or error message.


Testing :

To run tests, make sure your virtual environment is activated and then execute:
  python -m pytest tests/test_payments.py


Run the Tkinter GUI (Optional) :
  To run the tkinter GUI application, execute:
  python payment_interface.py



