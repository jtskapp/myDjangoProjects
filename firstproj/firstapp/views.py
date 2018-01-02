from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic, WebPage, RecordAccess, User
from firstapp.forms import NewUserForm

#Test get OS Env
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    #return HttpResponse("Hello World !!!<p>{}".format(BASE_DIR))
    my_dict = {
        'insert_data1': "Hello World !!! {}".format(BASE_DIR),
        'insert_data2': __file__,
    }
    return render(request,'firstapp/index.html', context = my_dict)


def sample(request):
    web_page_list = RecordAccess.objects.order_by('last_access')
    lastaccess = {
        'table_name': 'Web_Page_List',
        'access_records': web_page_list
    }
    return render(request,'firstapp/sample.html', context = lastaccess)


def users(request):
    user_list = User.objects.order_by('first_name','last_name')
    userlist = {
        'table_name': 'User_List',
        'user_list': user_list
    }
    return render(request, 'firstapp/users.html', context = userlist)

def user2(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Invalid Form')

    return render(request, 'firstapp/user2.html', context = {'NewUserForm': NewUserForm})
