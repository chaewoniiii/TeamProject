from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('movie_list', views.movie_list, name='movie_list'),
    path('movie_info/<mcd>/', views.movie_info, name='movie_info')
]
