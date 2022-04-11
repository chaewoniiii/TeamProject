import imp
from multiprocessing import context
from time import time
from django.shortcuts import redirect, render
from rating_board import views as rt_list
from .models import Movie
from datetime import datetime, timedelta
from django.core.paginator import Paginator

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
    
    moviedata = Movie.objects.all().order_by('-released_date')
    context = {}
    now = datetime.now()
    before_now = now - timedelta(days=60)
    now_movie = moviedata.filter(released_date__gte = before_now)
    paginator = Paginator(now_movie, 4)
    page_number = request.GET.get('p')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'movie_list.html', {'moviedata':page_obj})

