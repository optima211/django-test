from . import views
from django.urls import path, re_path
from django.views.generic import DetailView
from admin123.models import Admins

app_name = 'admin123'
urlpatterns = [
    # path('', ListView.as_view(queryset=Admins.objects.all().order_by("-date")[:20],
    #                           template_name="admin123/admin-select.html")),
    # path('', views.index, name='index'),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Admins, template_name="admin123/admin-select.html")),
    path('', views.ShowUsersView.as_view(template_name="admin123/admin-select.html")),
    # path('Admins/<int: pk>/',
    #      views.UsersDetailView.as_view(template_name="admin123/admin-select.html", name='users-detail')),
    # path('admin123/add/',
    #      views.CreateUsersView.as_view(template_name="admin123/admin-select.html", name='users-add')),
    path('create/', views.AdminsCreateView.as_view(), name='post_new'),
    # path('<int:pk>/', views.AdminDetailView.as_view(), name='detail'),
]
