from django.contrib import admin
from .models import Seat_info, Ticket
# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pay','number_people','userId','movie_code',)

class SeatAdmin(admin.ModelAdmin):
    list_display = ('res_check',)

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Seat_info, SeatAdmin)