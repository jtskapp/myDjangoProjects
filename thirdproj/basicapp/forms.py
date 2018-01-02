from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name has to start with Z')

class FirstForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[validators.EmailValidator])
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verifyemail = all_clean_data['verify_email']

        if email != verifyemail:
            raise forms.ValidationError("Your email not matching !!!")

    # botchatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxValueValidator(0)])
    # def clean_botchatcher(self):
    #     botchatcher = self.cleaned_data['botchatcher']
    #     if len(botchatcher) > 0:
    #         raise forms.ValidationError("Catch Bot !!!")
