#Django imports
from django.contrib import admin

#App imports
from f1rest.teams.models import Team

class TeamAdmin(admin.ModelAdmin):
    """
    Admin to Team model
    """
    list_display = ('name','full_name','active',)
    list_filter = ('active',)
    ordering = ('name',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(Team,TeamAdmin)
