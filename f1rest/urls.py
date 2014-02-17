# Django imports
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

#App imports
from f1rest.teams.views import TeamViewSet
from f1rest.drivers.views import DriverViewSet
from f1rest.races.views import RaceViewSet, SeasonViewSet, GrandPrixViewSet
from f1rest.countries.views import CountryViewSet

#Admin auto
admin.autodiscover()

#Rest router register
router = routers.DefaultRouter()
router.register(r'teams',TeamViewSet)
router.register(r'drivers',DriverViewSet)
router.register(r'races',RaceViewSet)
router.register(r'seasons',SeasonViewSet)
router.register(r'grandprixs',GrandPrixViewSet)
router.register(r'countries',CountryViewSet)

urlpatterns = patterns('',
    url(
        r'^',
        include(router.urls)
    ),
    url(
        r'^admin/',
        include(admin.site.urls)
    ),
)
