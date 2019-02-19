# from . import views
from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from admin123.models import Admins

urlpatterns = [
    path('', ListView.as_view(queryset=Admins.objects.all().order_by("-date")[:20],
                              template_name="admin123/admin-select.html")),
    # path('', views.index, name='index'),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Admins, template_name="admin123/admin-select.html")),
]
