from django.urls import path, include
from . import views

app_name = "Rating"

urlpatterns = [
    path('rt_create/', views.rt_create, name='rt_create'),
    path('rt_list/', views.rt_list, name='rt_list')
]
