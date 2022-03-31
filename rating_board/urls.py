from django.urls import path, include
from . import views

urlpatterns = [
    path('rt_create/', views.rt_create)
]
