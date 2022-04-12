from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

def home(request):

    return render(request, "home.html")

@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        birthday = request.POST['birthday']
        phoneNum = request.POST['phoneNum']
        email = request.POST['email']
        userId = request.POST['userId']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if not (username and birthday and phoneNum and email and userId and password and re_password):  
            res_data['error'] = '모든 값을 입력해야 합니다'
        elif password != re_password:
            res_data['password_error'] = '비밀번호가 다릅니다'
        else:
            user = User(
                username = username,
                birthday = birthday,
                phoneNum = phoneNum,
                email = email,
                userId = userId,
                password = make_password(password),
            )
        
            user.save()
            return render(request, 'registerOk.html', res_data)

        return render(request, 'register.html', res_data)

@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        userId = request.POST.get('userId', None)
        password = request.POST.get('password', None)

        res_data = {}
        if not(userId and password):
            res_data['error'] = '모든 값을 입력해야 합니다.'
        else:
            try:
                user = User.objects.get(userId=userId)
            except AttributeError:
                res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다'
            except ObjectDoesNotExist:
                res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다'
            except UnboundLocalError:
                res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다'
            try:
                if check_password(password, user.password):
                    request.session['user'] = user.id
                    return redirect('/')
            except UnboundLocalError:
                res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다.'
            try:
                if password != user.password:
                    res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다.'
            except UnboundLocalError:
                res_data['login_error'] = '아이디(또는 비밀번호)를 잘못입력하셨습니다.'

        return render(request, 'login.html', res_data)
        
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return render(request, 'logout.html')

def idchk(request):
        userId = request.GET.get('userId')
        if not userId:
            idchk = 'fail'
            
        else:
            try:
                u = User.objects.get(userId = userId)
            except:
                u = None
            if u is None:
                idchk = "pass"
            else:
                idchk = "fail"
        context = {'idchk': idchk}
        
        return JsonResponse(context)