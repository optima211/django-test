from django.shortcuts import render
from django.views.generic import ListView
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
