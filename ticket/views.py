from django.shortcuts import render, redirect
from .models import Ticket
from movieAdmin.models import Area_info, Branch_office
from movie.models import Movie, Ticket_info

def ticket_book(request):
    if not request.session.get('user'):
        return render(request, 'bookOk.html', {'error': 3})

    all_movies = Movie.objects.all()
    all_tickets = Ticket_info.objects.all()
    all_areas = Area_info.objects.all()
    all_branches = Branch_office.objects.all()

    context = {
        'movies': all_movies,
        'tickets': all_tickets,
        'areas': all_areas,
        'branches': all_branches,
    }
    if request.method == 'POST':
       a = request.POST.get('adult',0)
       b = request.POST.get('teenager',0)
       c = request.POST.get('kid',0)
       print(a, b, c)
    # adult =
    # teenager =
    # kid =

    # pay = adult * 12000 + teenager * 9000 + kid * 6000
    # number_people = adult + teenager + kid
    # userId = request.session.get('user')
    # movie_code = request.GET['ticket']

    # ticket = Ticket(pay=pay, number_people=number_people, userId=userId, movie_code=movie_code)
    # ticket.save()

    return render(request, 'ticket_book.html', context)

def ticket_check(request):
    return render(request, 'ticket_check.html')