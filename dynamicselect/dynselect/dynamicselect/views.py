from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from .models import Continent, Country, Location
# Create your views here.
def index(request):
 return render(request, 'dynamicselect/addform.html')

def get_json_data(request):
 json_data = ''
 if request.method == 'GET' and 'continent' in request.GET:
  continent = request.GET.get('continent', None)
  print(continent)
  if continent:
   json_data = Country.objects.filter(continent__name=continent)#.values('name').distinct()
   json_data = serializers.serialize("json", json_data)
   # current_tag = Tag.objects.get(pk=tag)
   # parents = Tag.objects.all().filter(parent__lt=current_tag)

 if request.method == 'GET' and 'country' in request.GET:
    country = request.GET.get('country', None)
    print(country)
    if country:
     json_data = Location.objects.filter(country__name=country)#.values('city','street').distinct()
     json_data = serializers.serialize("json", json_data)
     #json_data = serializers.serialize("json", location_objects)

 return JsonResponse({'json_data': json_data})
 #return JsonResponse(json_data, content_type="application/javascript")
