import os
from flask import Flask, render_template, redirect, request
import stripe

app = Flask(__name__)

stripe.api_key = 'sk_test_...'  # Inserisci la tua chiave segreta di test

YOUR_DOMAIN = 'https://climaadvisor.onrender.com'  # Modifica dopo la pubblicazione

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Report ClimaAdvisor™',
                },
                'unit_amount': 999,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return redirect(session.url, code=303)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')
