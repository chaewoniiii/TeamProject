from django.contrib import admin
from .models import Payinfo
# Register your models here.
class PayAdmin(admin.ModelAdmin):
    list_display = ('people', 'price',)



admin.site.register(Payinfo, PayAdmin)


