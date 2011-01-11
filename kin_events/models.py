from django.db import models

class Event(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, help_text='Area/Zone or Quest Title')
    players = models.CharField(max_length=200, blank=True, help_text='eg. 3+ players, levels 45-52')
    date = models.DateTimeField('event date')
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return self.title