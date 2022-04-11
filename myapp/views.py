from datetime import datetime, timedelta
import imp
from django.shortcuts import redirect, render
from movie.models import Movie
from user.models import User
from django.core.paginator import Paginator
# Create your views here.
def index(request):
        try:
                user_id = request.session.get('user')
                user = User.objects.get(pk=user_id)
                request.session['userid'] = user.userId
        except User.DoesNotExist:
                pass
        moviedata = Movie.objects.all().order_by('-released_date')
        context = {}
        now = datetime.now()
        before_now = now - timedelta(days=15)
        now_movie = moviedata.filter(released_date__gte = before_now)
        paginator = Paginator(now_movie, 1)
        page_number = request.GET.get('p')
        page_obj = paginator.get_page(page_number)

        context = {
                'movie' : page_obj,
                'movie_s' : now_movie
        }


        return render(request, 'home.html', context)