from django import forms
from basic.models import  Member, Order

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'
