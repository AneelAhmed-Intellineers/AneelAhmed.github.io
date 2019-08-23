from django.db import models


class Equity(models.Model):

    title = models.CharField(max_length=50)
    ticker = models.CharField(max_length=20)
    shares = models.IntegerField(null=True, blank=True, default=None)
    current_price = models.FloatField(null=True, blank=True, default=None)
    fx_rate = models.FloatField(null=True, blank=True, default=None)
    
    def __str__(self):

        return self.title


    def _get_current_value(self):

        return self.current_price * self.shares

    def _get_net_value(self):

        return self.current_value * self.fx_rate


    current_value = property(_get_current_value)
    net_value = property(_get_net_value)
