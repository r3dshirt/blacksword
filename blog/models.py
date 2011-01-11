from django.db import models

class Blog(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title