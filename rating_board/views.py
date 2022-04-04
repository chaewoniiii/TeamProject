from importlib.resources import contents
from multiprocessing import context
from traceback import print_tb
from django.http import Http404
from django.shortcuts import redirect, render
from .models import Rating_Board
from user.models import User
from movie.models import Movie
from ticket.models import Ticket
from django.core.paginator import Paginator

# Create your views here.

"""
    0 : 아무 문제 없음 정상 실행
    1 : 예매 안한 유저
"""

def rt_create(request,mcd):
    if not request.session.get('user'):     
        return redirect('/user/login/')

    if request.method == "POST":
        rt_board = Rating_Board()
        ticket = Ticket.objects.all()
        user_id = request.session.get('user')
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.get(pk=mcd)
        content = {
            'mcd':mcd
        }
        # 예매했을 경우에만 작성가능하게..
        ticket_chk = ticket.filter(movie_code=mcd, userId=user_id)
        if ticket_chk:
            rt_board.rating = float(request.POST['rating_star']) / 2
            rt_board.rating_content = request.POST['DOC_TEXT']
            rt_board.userId = user
            rt_board.movie_code = movie
            content.update({'error':0})
            rt_board.save()
            return render(request, 'rtOk.html', content)
        else:
            content.update({'error':1})
            return render(request, 'rtOk.html', content)


def rt_list(request, mcd):
    try:
        rt_board = Rating_Board()
        user_id = request.session.get('user')
        user = User.objects.get(pk=user_id)
        movie = Movie.objects.get(pk=mcd)
        rt_board_order = Rating_Board.objects.all().order_by('-pk')
        rt_filter = rt_board_order.filter(movie_code=mcd) 
        s = 0
        for i in rt_filter:
            s += i.rating
           
        write_pages = int(request.session.get('write_pages', 5))
        per_page = int(request.session.get('per_page', 5))    
        page = int(request.GET.get('p', 1))

        paginator = Paginator(rt_filter, per_page)    
        rating_page = paginator.get_page(page)          

        start_page = ((int)((rating_page.number - 1) / write_pages) * write_pages) + 1
        end_page = start_page + write_pages - 1

        if end_page >= paginator.num_pages:
            end_page = paginator.num_pages
        
        now_page = rating_page.number
        request.session['now_page'] = now_page
        string = str(user)
        content = {
            "rt_board" : rating_page,
            "rt_avg": s/rt_filter.count(),
            'pages' : write_pages,
            'start_page' : start_page,
            'end_page' : end_page,
            'page_range' : range(start_page, end_page + 1),
            'mcd' : movie.pk,
            'user' : user,
            'admin_chk' : string.startswith('admin'),
        }
        return render(request, 'rt_list.html', content)
        # return content

    except Movie.DoesNotExist:
        return Http404('없는 정보')

def rt_listall(request):
    user_id = request.session.get('user')
    user = User.objects.get(pk=user_id)
    adminchk = str(user).startswith('admin')
    if not adminchk:
        return redirect('/')

    rtb = Rating_Board.objects.all().order_by('movie_code')

    write_pages1 = int(request.session.get('write_pages1', 10))
    per_page1 = int(request.session.get('per_page1', 10))    
    page = int(request.GET.get('p', 1))

    paginator = Paginator(rtb, per_page1)    
    rating_page = paginator.get_page(page)          
    
    start_page = ((int)((rating_page.number - 1) / write_pages1) * write_pages1) + 1
    end_page = start_page + write_pages1 - 1

    if end_page >= paginator.num_pages:
        end_page = paginator.num_pages
    
    now_page = rating_page.number
    request.session['now_page1'] = now_page
    
    content = {
        "rt_board" : rating_page,
        'write_pages': write_pages1,
        'start_page': start_page,
        'end_page': end_page,
        'page_range' : range(start_page, end_page + 1),
    }
    
    return render(request, 'rt_listall.html', content)


def rt_delete(request):
    if request.method == "POST":
        try:
            id = request.POST['id']
            rtb = Rating_Board.objects.get(pk=id)
            d_mcd = request.POST['d_mcd']
            rtb.delete() 
        except Rating_Board.DoesNotExist:
            return Http404('없는 글 입니다')
            
        return render(request, 'rt_deleteOk.html', {'mcd':d_mcd})