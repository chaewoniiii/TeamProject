from django.urls import path, include
from . import views

app_name = 'Madmin'

urlpatterns = [
    path('', views.movieAdminMain, name='admin_main'),
    path("movie_management/", views.movie_management, name="movie_management"),
    path("admin_newlist/", views.admin_newlist, name="admin_newlist"),
    path("admin_userchk/", views.admin_userchk, name="admin_userchk"),
]
