from django.contrib import admin
from .models import Rating_Board

# Register your models here.
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating_content',)


# admin.site.register(Rating_Board, RatingAdmin)

admin.site.register(Rating_Board, RatingAdmin)

