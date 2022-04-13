from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import requests
import json
from ticket.models import Ticket
from user.models import User
from movie.models import Movie
from .models import Payinfo
from datetime import datetime, timedelta


# Create your views here.
def pay(request):
    now = datetime.now()
    global username
    global partner_order_id
    global item_name
    all_movies = Movie.objects.all()
    userpk = request.session['user']
    username = User.objects.get(pk=userpk)
    
    if request.method == "POST":
        adult = int(request.POST.get('adult',0))
        teenager = int(request.POST.get('teenager',0))
        kid = int(request.POST.get('kid',0))
        number_people = adult + teenager + kid

        default_amount = adult * 12000 + teenager * 9000 + kid * 6000

        request.session['adult'] = adult
        request.session['teenager'] = teenager
        request.session['kid'] = kid

        if now.year > 10:
            total_amount = int(default_amount - (default_amount * 0.2))
        else:
            total_amount = default_amount

        movie_pk = request.POST.get('movie_choice')
        s = all_movies.filter(pk=movie_pk)
        for i in s:
            item_name =i
            partner_order_id = i.pk
        request.session['ticket_pay'] = total_amount
        request.session['ticket_number_people'] = number_people
        
        Base_url = 'http://127.0.0.1:8000/kakaopay/'
        URL = 'https://kapi.kakao.com/v1/payment/ready'

        headers = {
            # "Authorization": "KakaoAK " + "Kakao Developers에서 생성한 앱의 어드민 키",   # 변경불가
            "Authorization": "KakaoAK " + "f906237801ca96fbefc1f91503338232",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 코드
            "partner_order_id": partner_order_id,     # 영화코드
            "partner_user_id": username,    # 유저 아이디
            "item_name": item_name,        # 영화 제목
            "quantity": number_people,                # 인원수
            "total_amount": total_amount,        # 가격 : 인원수 * 영화표 가격 (기본 10000)
            "tax_free_amount": "0",         # 구매 물품 비과세
            "approval_url": Base_url + "payOk",
            "cancel_url": Base_url + "payCancel",
            "fail_url": Base_url + "payFail",
        }
        
        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']      # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']   # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)
    
    return render(request, 'pay.html')


def payOk(request):

    userpk = request.session['user']
    username = User.objects.get(pk=userpk)
    tickt = Ticket()
    movie_code = Movie.objects.get(pk=partner_order_id)
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "f906237801ca96fbefc1f91503338232",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 코드
        "tid": request.session['tid'],  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": partner_order_id,     # 영화코드
        "partner_user_id": username,    # 유저 아이디
        "pg_token": request.GET.get("pg_token"),     # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
        'user': username,
        'adult': request.session['adult'],
        'teenager': request.session['teenager'],
        'kid': request.session['kid'],
    }
    tickt.pay = request.session['ticket_pay']
    tickt.number_people = request.session['ticket_number_people']
    tickt.userId = username
    tickt.movie_code = movie_code
    tickt.save()

    return render(request, 'payOk.html', context)
    

def payres(request):
    return render(request, 'payres.html')