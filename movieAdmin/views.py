from multiprocessing import context
from django.shortcuts import redirect, render
from user.models import User
from movie.models import Movie
from news import views as news_view

# Create your views here.
def movieAdminMain(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    user_id = request.session.get('user')
    user = User.objects.get(pk=user_id)
    adminchk = str(user).startswith('admin')

    context = {}
    context.update({
        "news":news_view.share_news_list(request)['news'],
        })
    
    if adminchk:
        return render(request, 'movie_adminMain.html', context)
    else: 
        return redirect('/')

def movie_management(request): # 영화 모델 추가하고 여기도 영화 DB를 똑같이 movie app 처럼 가져와서 씀
   moviedata = Movie.objects.all()
   return render(request, 'movie_management.html', {'moviedata': moviedata})


