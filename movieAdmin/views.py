from multiprocessing import context
from django.shortcuts import redirect, render
from user.models import User
from movie.models import Movie
from news import views as news_view
from django.core.paginator import Paginator
# Create your views here.

def admin_newlist(request):
    
    context = {}
    context.update({
        "news":news_view.share_news_list(request)['news'],
        })

    return render(request, 'admin_newlist.html',context)

def movieAdminMain(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    user_id = request.session.get('user')
    user = User.objects.get(pk=user_id)
    adminchk = str(user).startswith('admin')
    
    
    if adminchk:
        return render(request, 'movie_admin.html')
    else: 
        return redirect('/')

def movie_management(request): # 영화 모델 추가하고 여기도 영화 DB를 똑같이 movie app 처럼 가져와서 씀
   moviedata = Movie.objects.all().order_by('-released_date')

   per_page = int(request.session.get('per_page', 10))    
   page = int(request.GET.get('p', 1))
   paginator = Paginator(moviedata, per_page)  
   movie_paing = paginator.get_page(page) 
   write_pages = int(request.session.get('write_pages', 10)) 
   start_page = ((int)((movie_paing.number - 1) / write_pages) * write_pages) + 1
   end_page = start_page + write_pages - 1

   if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
   context = {
       'moviedata' : movie_paing,
       'write_pages': write_pages,
       'start_page': start_page,
       'end_page': end_page,
       'page_range' : range(start_page, end_page + 1),
   }

   return render(request, 'movie_management.html', context)

def admin_userchk(request):
    user = User.objects.all().order_by('-pk')
    context = {
        'user':user
    }
    if request.method == 'POST':
        context.update({'userinfo': 1})
        return render(request,'admin_userchk.html', context)
    return render(request, 'admin_userchk.html', context)


def movie_insert(request):
    moviedata = Movie.objects.all()
    return render(request, 'movie_insert.html', {'moviedata': moviedata})