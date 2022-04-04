from django.contrib import admin
from .models import Movie
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_code', 'movie_title',)


admin.site.register(Movie, MovieAdmin)