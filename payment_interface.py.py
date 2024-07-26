import tkinter as tk
from tkinter import messagebox
import requests


API_URL = "http://127.0.0.1:8000"  

class PaymentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stripe Payment Test")

        
        self.create_widgets()

    def create_widgets(self):
        # Card number
        tk.Label(self.root, text="Card Number:").grid(row=0, column=0, padx=10, pady=10)
        self.card_number_entry = tk.Entry(self.root)
        self.card_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Expiry month
        tk.Label(self.root, text="Expiry Month:").grid(row=1, column=0, padx=10, pady=10)
        self.exp_month_entry = tk.Entry(self.root)
        self.exp_month_entry.grid(row=1, column=1, padx=10, pady=10)

        # Expiry year
        tk.Label(self.root, text="Expiry Year:").grid(row=2, column=0, padx=10, pady=10)
        self.exp_year_entry = tk.Entry(self.root)
        self.exp_year_entry.grid(row=2, column=1, padx=10, pady=10)

        # CVC
        tk.Label(self.root, text="CVC:").grid(row=3, column=0, padx=10, pady=10)
        self.cvc_entry = tk.Entry(self.root)
        self.cvc_entry.grid(row=3, column=1, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit Payment", command=self.submit_payment)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Result label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=20)

    def submit_payment(self):
        card_number = self.card_number_entry.get()
        exp_month = self.exp_month_entry.get()
        exp_year = self.exp_year_entry.get()
        cvc = self.cvc_entry.get()

        if not (card_number and exp_month and exp_year and cvc):
            messagebox.showerror("Error", "All fields are required!")
            return

        
        data = {
            "number": card_number,
            "exp_month": int(exp_month),
            "exp_year": int(exp_year),
            "cvc": cvc
        }

        try:
            response = requests.post(f"{API_URL}/payments/create", json=data)
            response.raise_for_status() 
            result = response.json()
            self.result_label.config(text=f"Payment Successful: {result}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Payment failed: {e}")
            self.result_label.config(text="Payment Failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()
