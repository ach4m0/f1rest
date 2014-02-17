#Django imports
from django.db import models

#App imports
from f1rest.teams.models import Team
from f1rest.countries.models import Country

DRIVER_TYPE_CHOICES = (
    ('FD','First Driver'),
    ('SD','Second Driver'),
    ('TD','Test Driver'),
)

class Driver(models.Model):
    """
    Class to encapsulate all driver information
    """
    active = models.BooleanField(default=True)
    birthday = models.DateField()
    championships = models.IntegerField(default=0)
    driver_type = models.CharField(max_length=2,choices=DRIVER_TYPE_CHOICES)
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country)
    shortname = models.CharField(max_length=5)
    team = models.ForeignKey(Team, null=True)

    def __unicode__(self):
        return u'{0} - {1} [{2}]'.format(self.shortname, self.name, self.team.name)

