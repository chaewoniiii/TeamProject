from datetime import datetime, timedelta
from turtle import title
from django.shortcuts import render, redirect
from .models import Ticket
from movieAdmin.models import Area_info, Branch_office
from movie.models import Movie, Ticket_info
from user.models import User

def ticket_book(request):
    if not request.session.get('user'):
        return render(request, 'bookOk.html', {'error': 3})
    else:
        all_movies = Movie.objects.all()
        all_tickets = Ticket_info.objects.all()
        all_areas = Area_info.objects.all()
        all_branches = Branch_office.objects.all()

        now = datetime.now()
        before_now = now - timedelta(days=30)
        now_movie = all_movies.filter(released_date__gte = before_now)
        
        context = {
            'movies': now_movie,
            'tickets': all_tickets,
            'areas': all_areas,
            'branches': all_branches,
        }


        if request.method == 'POST':
            movie_pk = request.POST.get('movie_choice')
            print(Movie.objects.get(pk=movie_pk))

        return render(request, 'ticket_book.html', context)

def ticket_check(request):
    return render(request, 'ticket_check.html')