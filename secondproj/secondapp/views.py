from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("<em>My Second App</em>")


def help(request):
	data = {
		'insert_data': "Help Page"
	}
	return render(request,"secondapp/help.html", context=data
