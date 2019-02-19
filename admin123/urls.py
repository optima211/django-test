from . import views
from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from news.models import Admins

urlpatterns = [
    path('', ListView.as_view(queryset=Admins.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    # path('', views.index, name='index'),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Admins, template_name="admin123/admin-select.html")),
]
