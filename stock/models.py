from django.db import models


class Equity(models.Model):

    title = models.CharField(max_length=50)
    ticker = models.CharField(max_length=20)
    shares = models.IntegerField(null=True, blank=True, default=None)
    
    def __str__(self):

        return self.title
