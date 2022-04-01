from django.urls import path
from . import views

app_name = "Ticket"

urlpatterns = [
    path('ticket_book/', views.ticket_book, name='ticket_book'),
    path('ticket_check/', views.ticket_check, name='ticket_check'),
]