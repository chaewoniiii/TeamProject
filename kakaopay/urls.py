from django.urls import path
from . import views

app_name = 'Kakao'

urlpatterns = [
    path('',views.pay, name='pay'),
    path('payOk/', views.payOk, name='payOk'),
    path('payCancel/', views.payres, name='payres')
]
