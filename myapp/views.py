from django.shortcuts import redirect, render
from user.models import User

# Create your views here.
def index(request):
    if not request.session.get('user'):
        return render(request, 'home.html',{"user":""})
    else:
        user_id = request.session.get('user')
        user = User.objects.get(pk=user_id)
        request.session['userid'] = user.username
        return render(request, 'home.html')