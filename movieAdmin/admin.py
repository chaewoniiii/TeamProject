from django.contrib import admin

from movieAdmin.models import Area_info, Branch_office

# Register your models here.
class AreaAdmin(admin.ModelAdmin):
    list_display = ('area',)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name','area',)

admin.site.register(Area_info, AreaAdmin)
admin.site.register(Branch_office, BranchAdmin)