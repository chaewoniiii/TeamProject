from importlib.resources import contents
from django.http import Http404
from django.shortcuts import redirect, render
from .models import News
from user.models import User
from .forms import NewsForm
from django.core.paginator import Paginator

# Create your views here.
def share_news_list(request):
    all_news = News.objects.all().order_by('-pk')
        
    per_page = int(request.session.get('per_page', 2))    
    page = int(request.GET.get('p', 1))

    paginator = Paginator(all_news, per_page)    
    news_board = paginator.get_page(page)          

    context = {
        'news': news_board,
    }

    return context

def news_list(request):

    user_id = request.session.get('user') 
  
    context = share_news_list(request)
    
    try:
        user = User.objects.get(pk=user_id)
        
    except User.DoesNotExist:
         pass
  
    return render(request, 'news_list.html', context)



def news_detail(request,pk):
    try:
        user_id = request.session.get('user') 
        nwd = News.objects.get(pk=pk)
        nwd.news_views += 1
        nwd.save()
        now_page = int(request.session.get('now_page'))
        content = {
            'nwd' : nwd,
            'now_page' : now_page,
        }
        try:
            user = User.objects.get(pk=user_id)
            content.update({"userchk":str(user).startswith('admin')})
        except User.DoesNotExist:
            pass
    except News.DoesNotExist:
        return Http404('없는 게시글')

    return render(request, 'news_detail.html', content)


def news_create(request):
    
    user_id = request.session.get('user') 
    user = User.objects.get(pk=user_id)

    if not request.session.get('user'):     
        return redirect('/user/login/')

    # 혹시 일반 유저가 들어와서 공지추가 글쓰기를 눌렀을 경우
    if not str(user).startswith('admin'):
        return redirect('/')

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News()
            news.news_title = form.cleaned_data['title']
            news.news_content = request.POST['news_content']
            news.admins = user
            news.save()  
            return redirect('/news/news_list/')
    else:
        form = NewsForm()

    return render(request, 'news_create.html', {'form': form})

def news_update(request, pk):
    if request.method == "POST":
        try:
            nwd = News.objects.get(pk=pk)
            nwd.news_title = request.POST['news_title']
            nwd.news_content = request.POST['news_content']
            nwd.save()
            return redirect('/news/news_list/')
        except News.DoesNotExist:
            return Http404("게시글 찾을 수 없음")
    else:
        nwd = News.objects.get(pk=pk)
        return render(request, 'news_update.html', {'nwd':nwd})

def news_delete(reqeust):
    if reqeust.method == "POST":
        id = reqeust.POST['id']
        nwd = News.objects.get(pk=id)
        nwd.delete()
    return render(reqeust, 'news_delete.html')