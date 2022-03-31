from django.http import Http404
from django.shortcuts import redirect, render
from .models import News
from user.models import User
from .forms import NewsForm
from django.core.paginator import Paginator

# Create your views here.
def news_list(request):

    all_news = News.objects.all().order_by('-pk')

    # page = int(request.GET.get('p',1))
    # paginator = Paginator(all_news, 10) 
    # news_board = paginator.get_page(page)  
    
    write_pages = int(request.session.get('write_pages', 5))
    per_page = int(request.session.get('per_page', 10))    
    page = int(request.GET.get('p', 1))

    paginator = Paginator(all_news, per_page)    
    news_board = paginator.get_page(page)          

    start_page = ((int)((news_board.number - 1) / write_pages) * write_pages) + 1
    end_page = start_page + write_pages - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
    
    now_page = news_board.number
    request.session['now_page'] = now_page
 

    context = {
        'news': news_board,
        'write_pages': write_pages,
        'start_page': start_page,
        'end_page': end_page,
        'page_range' : range(start_page, end_page + 1),
    }
    
    return render(request, 'news_list.html', context)


def news_detail(request,pk):
    try:
        nwd = News.objects.get(pk=pk)
        nwd.news_views += 1
        nwd.save()
    except News.DoesNotExist:
        return Http404('없는 게시글')

    return render(request, 'news_detail.html', {"nwd": nwd})


def news_create(request):
    # 현재 로그인 한 상태인지 확인
    if not request.session.get('user'):     
        return redirect('/user/login/')     

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News()
            user_id = request.session.get('user') 
            user = User.objects.get(pk=user_id)
            news.news_title = form.cleaned_data['title']
            news.news_content = request.POST['news_content']
            news.admins = user
            news.save()  


            return redirect('/news/news_list/')

    else:
        form = NewsForm()
    
    return render(request, 'news_create.html', {'form': form})