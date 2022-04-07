from django.shortcuts import redirect, render
from user.models import User

# Create your views here.
def movieAdminMain(request):
    if not request.session.get('user'):
        return redirect('/user/login/')
    user_id = request.session.get('user')
    user = User.objects.get(pk=user_id)
    adminchk = str(user).startswith('admin')
    if adminchk:
        return render(request, 'movie_adminMain.html')
    else: 
        return redirect('/')