from django.shortcuts import render
from basicapp.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'basicapp/index.html', context={'name':'home'})


# def login(request):
#     return render(request,'basicapp/login.html', context={'name':'login'})


def registration(request):
    registered = False

    if request.method == "POST":
        # Is POST Method
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            #process user form
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #process user profile forms
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Not POST Method
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # return render(request,'basicapp/registration.html', context={'name':'registration',
    #                                                     'user_form': user_form,
    #                                                     'profile_form': profile_form,
    #                                                     'registered': registered
    #                                                })
    if registered:
        return HttpResponseRedirect(reverse('user_login'))
    else:
        return render(request,'basicapp/registration.html', context={'name':'registration',
                                                            'user_form': user_form,
                                                            'profile_form': profile_form,
                                                            'registered': registered})


# user logout views
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# validate login_required
@login_required
def validate_login(request):
    return HttpResponse("You're Login !!! Congratulations !!!")

# user Login view
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled !!!")
        else:
            print("Login attempt failed !!!")
            print("UserName : {} and Password : {}".format(username,password))

    else:
        return render(request,'basicapp/login.html')
