from django.contrib import admin
from .models import Movie, Ticket_info
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'title',)


class MovieTick(admin.ModelAdmin):
    list_display = ('start_time',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Ticket_info, MovieTick)