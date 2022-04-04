from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk','username' ,'userId', 'password')

admin.site.register(User, UserAdmin)
