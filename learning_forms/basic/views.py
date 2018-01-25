from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from basic.models import Member, Profile, Order
from basic.forms import OrderForm, UserForm, ProfileForm
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>This is a test landing page !!!</h1>')


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
        return render(request,'login.html')


@login_required(login_url='user_login')
def orderform1(request):
    ordered = False
    if request.method == "POST":
        # Is POST Method
        order_form = OrderForm(data=request.POST)

        if order_form.is_valid():

            #process order form
            order = order_form.save(commit=True)
            ordered = True
        else:
            print(order_form.errors)
    else:
        # Not POST Method
        order_form = OrderForm()

    if ordered:
        messages.success(request,'Order Submitted !!!')
        return reverse('orderform1')
    else:
        messages.info(request,'Please submit an order !!!')
        return render(request,'basic/orderform1.html', context={'NewOrderForm':order_form})


@login_required(login_url='user_login')
def orderform2(request):
    ordered = False
    if request.method == "POST":
        # Is POST Method
        order_form = OrderForm(data=request.POST)

        if order_form.is_valid():

            #process order form
            order = order_form.save(commit=True)
            ordered = True
        else:
            print(order_form.errors)
    else:
        # Not POST Method
        order_form = OrderForm()

    if ordered:
        messages.error(request,'Order Submitted !!!')
        return reverse('basic/orderform2.html')
    else:
        return render(request,'basic/orderform2.html', context={'NewOrderForm':order_form})


def userinfo(request):
    template_name = 'basic/userinfo.html'
    return render(request,template_name)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profiles)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('userinfo')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profiles)

    return render(request, 'basic/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def get_orders(request):
    print('in get_orders')
    search_data = request.GET.get('searchdata', None)
    data_found = list(Order.objects.filter(description__contains=search_data).values().order_by('member_id'))
    if data_found:
        data = { 'data_found' : data_found}
        messages.add_message(request, messages.INFO, '{} records found'.format(len(data_found)))
    else:
        messages.add_message(request, messages.ERROR, '0 records found !!!')

    return JsonResponse(data, safe=False)


def orderinfo(request):
    template_name = 'basic/orderinfo.html'
    return render(request,template_name)
