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
       adult = int(request.POST.get('adult',0))
       teenager = int(request.POST.get('teenager',0))
       kid = int(request.POST.get('kid',0))

       pay = adult * 12000 + teenager * 9000 + kid * 6000
       number_people = adult + teenager + kid

       movie_code = request.POST.get('ticket')

       userId = request.session.get('user')
       ticket = Ticket(pay=pay, number_people=number_people, userId=userId, movie_code=movie_code)
       ticket.save()

    return render(request, 'ticket_book.html', context)

def ticket_check(request):
    return render(request, 'ticket_check.html')