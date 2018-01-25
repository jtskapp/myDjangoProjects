from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)

from django.http import HttpResponse
from basicapp import models
from basicapp.forms import SchoolForm
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


class SchoolListView(ListView, UpdateView):
    context_object_name = 'schools'
    model = models.School
    form_class = SchoolForm

    success_url = '/basicapp/'

    def form_valid(self, form):
        form.save()
        return super(SchoolListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SchoolListView, self).get_context_data(**kwargs)
        context['school'] = models.School.objects.all()
        return context

# class SchoolListView(ListView):
#     context_object_name = 'schools'
#     model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basicapp/school_detail.html'


class SchoolCreateView(CreateView):
    fields = '__all__'
    model = models.School


class SchoolUpdateView(UpdateView):
    template_name = 'basicapp/school_edit_form.html'
    form_class = SchoolForm
    success_url = '/basicapp/'

    def form_valid(self, form):
        form.save()
        return super(CreateOrder, self).form_valid(form)

# class SchoolUpdateView(UpdateView):
#     model = models.School
#     form_class = SchoolForm
#     template_name = 'basicapp/school_edit_form.html'
#
#     def dispatch(self, *args, **kwargs):
#         self.school_id = kwargs['pk']
#         return super(SchoolUpdateView, self).dispatch(*args, **kwargs)
#
#     def form_valid(self, form):
#         form.save()
#         school = models.School.objects.get(id=self.school_id)
#         return HttpResponse(render_to_string('basicapp/school_edit_form_success.html', {'school': school}))

# def SchoolUpdateView(request, school_id=None):
#     if school_id is None:
#         school = models.School()
#         template_title = _(u'Add School')
#     else:
#         school = get_object(profile.company.contact_set.all(), pk=school_id)
#         template_title = _(u'Edit Contact')
#     if request.POST:
#         if request.POST.get('cancel', None):
#             return HttpResponseRedirect('/')
#             form = SchoolForm(profile.company, request.POST, instance=contact)
#         if form.is_valid():
#             contact = form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = ContactsForm(instance=contact, company=profile.company)
#         variables = RequestContext(request, {'form':form, 'template_title': template_title})
#
#     return render_to_response("school_edit_form.html", variables)



class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basicapp:list')
