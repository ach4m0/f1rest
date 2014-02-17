#Django imports
from django.contrib import admin

#App imports
from f1rest.races.models import Race, Season, GrandPrix, TypeResults, Results

class RaceAdmin(admin.ModelAdmin):
    """
    Admin to Race model
    """
    list_display = ('name','circuit_name','country','active',)
    list_filter = ('active','country',)
    ordering = ('id',)
    search_fields = ('name','circuit_name','country',)

class SeasonAdmin(admin.ModelAdmin):
    """
    Admin to Season model
    """
    list_display = ('year','start_date','end_date','active',)
    list_filter = ('active',)
    ordering = ('year',)
    search_fields = ('year',)

class GrandPrixAdmin(admin.ModelAdmin):
    """
    Admin to GrandPrix model
    """
    list_display = ('race','season','race_datetime','qualify_datetime',)
    list_filter = ('season',)
    ordering = ('race_datetime',)

class TypeResultsAdmin(admin.ModelAdmin):
    """
    Admin to TypeResults model
    """
    list_display = ('position','type_result','points','season',)
    list_filter = ('season','type_result',)
    ordering = ('type_result','position',)

class ResultsAdmin(admin.ModelAdmin):
    """
    Admin to Results model
    """
    list_display = ('grandprix','driver','result','time',)
    list_filter = ('driver',)
    ordering = ('grandprix','driver','result',)


# Registering models and modeladmins
admin.site.register(Race, RaceAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(GrandPrix, GrandPrixAdmin)
admin.site.register(TypeResults, TypeResultsAdmin)
admin.site.register(Results, ResultsAdmin)
