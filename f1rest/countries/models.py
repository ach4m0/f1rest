from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return u'{0}'.format(self.name)
