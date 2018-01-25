from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

# Create your views here.
class UserListView(ListView):
    model = UserProfile
    template_name = 'basic/user_list.html'
    context_object_name = 'userprofile'
    paginate_by = 3
    queryset = UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['user_info']  = User.objects.all()
        # other code
        return context
    #
    # def userinfo(self):
    #     return User.objects.all()
    #
    # def userinfo1(self, pk):
    #     return User.objects.all()


# class UserDetailView(UserListView):
#
#     # def get_context_data(self, **kwargs):
#     #     pk = self.kwargs.get('pk', None)
#     #     context = super(UserDetailView, self).get_context_data(**kwargs)
#     #     context['user_info']  = User.objects.filter(pk=pk)
#     #     # other code
#     #     return context
#
#     # def get_queryset(self):
#     #     self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
#     #     return Book.objects.filter(publisher=self.publisher)
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         if request.GET.get('pk', '') != '':
#             context['user_info'] = User.objects.get(pk=request.GET.get('pk'))
#         return context
