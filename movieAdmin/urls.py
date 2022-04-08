from django.urls import path, include
from . import views

app_name = 'Madmin'

urlpatterns = [
    path('', views.movieAdminMain),
    path("movie_management/", views.movie_management, name="movie_management"),
]
