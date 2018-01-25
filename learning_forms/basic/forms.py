from django import forms
from django.contrib.auth.models import User
from basic.models import  Member, Order, Profile

class OrderForm(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'
        # widgets = {
        #     'description': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'My Shirt', 'required': True, 'label':'', } ),
        #     'size': forms.MultipleChoiceField( attrs={ 'class': 'form-control', 'placeholder': 'size', 'required': True, 'label':'',} ),
        #     'color': forms.MultipleChoiceField( attrs={ 'class': 'form-control', 'placeholder': 'color', 'required': True, 'label':'',} ),
        # }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('country', 'city')
