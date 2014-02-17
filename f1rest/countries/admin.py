#Django import
from django.contrib import admin

#App import
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Country, CountryAdmin)
