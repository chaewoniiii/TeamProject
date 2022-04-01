from django.shortcuts import render

def ticket_book(request):
    return render(request, 'ticket_book.html')

def ticket_check(request):
    return render(request, 'ticket_check.html')