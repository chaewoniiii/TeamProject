from django.shortcuts import render
from rating_board import views as rt_list
from .models import Movie


# Create your views here.
def movie_info(request,mcd):

    r = rt_list.rt_list(request, mcd)
    movie_title = Movie.objects.get(pk=mcd)
    content = {
        'movie' : mcd,
        'movie_title' : movie_title
    }
    for key,value in r.items():
        content.update({key:value})

    return render(request, 'movie_info.html', content)

def movie_list(request):
    movie_all = Movie.objects.all().order_by('-pk')
    return render(request, 'movie_list.html', {"movie": movie_all})