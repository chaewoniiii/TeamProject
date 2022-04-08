from django.urls import path, include
from . import views

app_name = "Rating"

urlpatterns = [
    path('rt_list/<int:pk>/', views.rt_list, name='rt_list'),
    path('rt_create/<int:pk>/', views.rt_create, name='rt_create' ),
    path('rt_delete/', views.rt_delete, name='rt_delete'),
    path('rt_listall/', views.rt_listall, name='rt_listall'),
    path('rt_update/<int:pk>/', views.rt_update, name='rt_update')
]
