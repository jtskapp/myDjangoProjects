from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import forms

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')


def form_view(request):
    form = forms.FirstForm()

    if request.method == 'POST':
        form = forms.FirstForm(request.POST)

        if form.is_valid():
            #do something LANGUAGE_CODE
            print("Validation success !!!")
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            textarea = form.cleaned_data['text']
            print("Name: {}".format(name))
            print("Email: {}".format(email))
            print("Text: {}".format(textarea))

    return render(request,'basicapp/formpage.html', context={'form': form})
