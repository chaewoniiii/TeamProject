from django.shortcuts import redirect, render
from .models import Rating_Board
from user.models import User


# # Create your views here.
def rt_create(request):
    if not request.session.get('user'):     
        return redirect('/user/login/')

    if request.method == "POST":
        rt_board = Rating_Board()
        user_id = request.session.get('user')
        user = User.objects.get(pk=user_id)
        rt_board.rating = float(request.POST['rating_star']) / 2
        rt_board.rating_content = request.POST['DOC_TEXT']
        rt_board.userId = user
        rt_board.save()
       
        return redirect('.')

    else:
        return render(request, 'rt_create.html')


def rt_list(request):

    rt_board = Rating_Board.objects.all().order_by('-pk')

    return render(request, 'rt_list.html', {"rt_board": rt_board})
