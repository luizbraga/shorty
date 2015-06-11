from django.db import models

from pyshorteners.shorteners  import Shortener

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    
    def shortIt(self):
        shortener = Shortener('GoogleShortener')
        return format(shortener.short(self.url))