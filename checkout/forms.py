from .models import Charge
from django import forms

#Form for user end
class OrderForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = (
            'full_name', 'phone_number'
            )

#Payment Form
class PaymentForm(forms.Form):
    
    #use list to generate months and years
    MONTH_CHOICES = [(i,i) for i in range(1,12)]
    YEAR_CHOICES = [(i,i) for i in range(2019,2036)]
    
    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)