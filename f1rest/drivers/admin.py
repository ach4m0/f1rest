#Django imports
from django.contrib import admin

#App imports
from f1rest.drivers.models import Driver

class DriverAdmin(admin.ModelAdmin):
    """
    Admin to Driver model
    """
    list_display = ('name','shortname','team','driver_type','country','active',)
    list_filter = ('active','team','driver_type',)
    ordering = ('name',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Driver,DriverAdmin)
