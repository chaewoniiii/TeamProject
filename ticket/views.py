from django.shortcuts import render, redirect
from .models import Ticket
from movieAdmin.models import Area_info, Branch_office
from movie.models import Movie, Ticket_info

def ticket_book(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

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

    return render(request, 'ticket_book.html', context)

def ticket_check(request):
    return render(request, 'ticket_check.html')