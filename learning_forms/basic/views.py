from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from basic.forms import OrderForm

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is a test landing page !!!</h1>')

def orderform(request):
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
        #return HttpResponseRedirect(reverse('user_login
        return HttpResponse('<h1>Order Submitted !!!</h1>')
    else:
        return render(request,'basic/orderform.html', context={'NewOrderForm':order_form})
