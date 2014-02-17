#Django imports
from django.db import models

#App imports
from f1rest.drivers.models import Driver
from f1rest.countries.models import Country

#Constant
TYPE_RESULTS = (
    ('FP1','Free Practice 1'),
    ('FP2','Free Practice 2'),
    ('FP3','Free Practice 3'),
    ('Q1','Qualify 1'),
    ('Q2','Qualify 2'),
    ('Q3','Qualify 3'),
    ('R','Race'),
)

class Race(models.Model):
    """
    Class to encapsulate all races information
    """
    active = models.BooleanField(default=True)
    circuit_length = models.IntegerField()
    circuit_name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)
    distance = models.IntegerField()
    lap_record_driver = models.CharField(max_length=20,null=True)
    lap_record_time = models.CharField(max_length=10,null=True)
    lap_record_year = models.IntegerField(null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Season(models.Model):
    """
    Class to encapsulate all seasons information
    """
    active = models.BooleanField(default=False)
    end_date = models.DateField()
    races = models.ManyToManyField(Race, through='GrandPrix')
    start_date = models.DateField()
    year = models.IntegerField()

    def __unicode__(self):
        return u'{0}'.format(self.year)

class GrandPrix(models.Model):
    """
    Class to join races and season and save dates information
    """
    season = models.ForeignKey(Season)
    race = models.ForeignKey(Race)
    gpresults = models.ManyToManyField('TypeResults',through='Results')
    race_datetime = models.DateTimeField()
    qualify_datetime = models.DateTimeField()
    practice1_datetime = models.DateTimeField()
    practice2_datetime = models.DateTimeField()
    practice3_datetime = models.DateTimeField()
    laps = models.IntegerField()

    def __unicode__(self):
        return u'{0} - {1}'.format(self.race, self.season)

class TypeResults(models.Model):
    """
    Class to encapsulate all posible results in a weekend
    """
    position = models.IntegerField()
    points = models.IntegerField(default=0)
    season = models.ForeignKey(Season)
    type_result = models.CharField(max_length=3,choices=TYPE_RESULTS)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.position,self.type_result, self.points)

class Results(models.Model):
    """
    Class to join grandprixs, drivers and results with time information
    """
    grandprix = models.ForeignKey(GrandPrix)
    driver = models.ForeignKey(Driver)
    result = models.ForeignKey(TypeResults)
    time = models.CharField(max_length=12)

    def __unicode__(self):
        return u'{0} // {1} // {2}'.format(self.grandprix, self.result, self.driver)
