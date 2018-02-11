from django.db import models
from django.apps import AppConfig


class testConfig(AppConfig):
    name = 'test'

# Create your models here.

class Currency(models.Model):
    ticker = models.CharField(('Currency ticker'), max_length=10)
    name = models.CharField(('Currency name'), max_length=10)
    priceUSD = models.FloatField(default = -1.0)
