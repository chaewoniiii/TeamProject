from django.shortcuts import render
from rating_board import views as rt_list
from .models import Movie


# Create your views here. 혹시 몰라서 원래 여기 views.py에 있던 코딩은 제거에 복사해놨어여!
def movie_info(request, pk):
    movie = Movie.objects.get(id=pk)
    rating_list = rt_list.rt_list(request, pk)
    context = {
        'movie':movie,
    }
    for key,value in rating_list.items():
        context.update({key:value})
        
    return render(request, 'movie_info.html', context)

def movie_list(request):
    moviedata = Movie.objects.all()[:8]
    return render(request, 'movie_list.html', {'moviedata': moviedata})