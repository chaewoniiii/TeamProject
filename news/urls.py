from unicodedata import name
from django.urls import path
from . import views

app_name = "News"

urlpatterns = [
    path('news_list/', views.news_list, name='news_list'),
    path('news_detail/<int:pk>/', views.news_detail, name='news_detail'),
    path('news_create/', views.news_create, name='news_create'),
]
