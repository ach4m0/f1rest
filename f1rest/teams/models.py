#Django imports
from django.db import models

class Team(models.Model):
    """
    Class to encapsulate information about teams
    """
    active = models.BooleanField(default=True)
    base = models.CharField(max_length=30)
    championships = models.IntegerField(default=0)
    chassis = models.CharField(max_length=20)
    engine = models.CharField(max_length=40)
    full_name = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    start_year = models.IntegerField()
    team_principal = models.CharField(max_length=50)
    technical_chief = models.CharField(max_length=50,null=True)
    tyres = models.CharField(max_length=15,default="Pirelli")

    def __unicode__(self):
        return u'{0} - {1}'.format(self.name, self.chassis)
