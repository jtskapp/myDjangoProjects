from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)

from django.http import HttpResponse
from basicapp import models
from django.urls import reverse, reverse_lazy

# Create your views here.
def index(request):
    data = {'name': 'index'}
    return render(request, 'basicapp/index.html', context=data)


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Base View')


class IndexView(TemplateView):
    template_name = 'basicapp/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'index'
        return context


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basicapp/school_detail.html'


class SchoolCreateView(CreateView):
    fields = '__all__'
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basicapp:list')
