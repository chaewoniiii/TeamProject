from django.urls import path, include
from . import views

app_name = 'Main'

urlpatterns = [
    path('', views.index, name='home')
]
