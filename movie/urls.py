from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path('movie_info/<mcd>/', views.movie_info, name='movie_info')
]
