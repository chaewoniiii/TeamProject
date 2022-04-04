from django.contrib import admin
from .models import Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pay','number_people','userId','movie_code',)


admin.site.register(Ticket, TicketAdmin)