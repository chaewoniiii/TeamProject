from django.shortcuts import render
from rating_board import views as rt_list

# Create your views here.
def movie_info(request,mcd):

    r = rt_list.rt_list(request, mcd)
    content = {
        'movie' : mcd,
    }
    for key,value in r.items():
        content.update({key:value})
    
    return render(request, 'movie_info.html', content)