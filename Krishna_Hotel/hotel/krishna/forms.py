# forms.py

from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount')
    card_number = forms.CharField(label='Card Number', max_length=16)
    # Add more fields as needed for your payment process
