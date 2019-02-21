from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from admin123.forms import AdminsCreateForm
from .models import Admins


# Create your views here.
def index(request):
    return render(request, 'admin123/admin-select.html')


class ShowUsersView(ListView):
    model = Admins
    template_name = 'admin123/admin-select.html'
    context_object_name = 'admins'
    ordering = ['-date']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ShowUsersView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница панели администратора'
        return ctx


# class UsersDetailView(DetailView):
#     model = Admins
#     template_name = 'admin123/admin-select.html'
#     context_object_name = 'post'
# class CreateUsersView(CreateView):
#     model = Admins
#     fields = ['login', 'password', 'right', 'info']

class AdminsCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': AdminsCreateForm()}
        return render(request, 'admin123/admin-create.html', context)

    def post(self, request, *args, **kwargs):
        form = AdminsCreateForm(request.POST)
        if form.is_valid():
            admins = form.save()
            admins.save()
            return HttpResponseRedirect(reverse_lazy('admins:detail', args=[admins.id]))
        return render(request, 'admin123/admin-create.html', {'form': form})
