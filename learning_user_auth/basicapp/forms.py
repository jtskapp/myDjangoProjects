from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

HIGHEST_EDUCATION = (
            ('Select your highest education', 'Select your highest education'),
                ('Primary', 'Primary'),
              ('Secondary', 'Secondary'),
              ('High School', 'High School'),
              ('Post Grad', 'Post Grad'),
              ('Poly', 'Poly'))

class UserForm(forms.ModelForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control btn-default','placeholder':'UserName'}))
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control btn-default','placeholder':'UserName@email.com'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control btn-default','placeholder':'********'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField(label='',widget=forms.TextInput(attrs={'class':'form-control btn-default','placeholder':'http://yoursite'}))
    #profile_pic = forms.ImageField()
    dob = forms.DateField(label='',widget=forms.SelectDateWidget(attrs={'class':'form-control btn-default'}))
    highest_education = forms.ChoiceField(label='',choices=HIGHEST_EDUCATION,
                    widget=forms.Select(attrs={'class':'form-control btn-default'}),
                    required = False, initial='Select your highest education'
                    )

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'dob', 'highest_education', 'profile_pic')
