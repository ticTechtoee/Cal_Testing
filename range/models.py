from django.db import models


class price_range(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)


class update_price(models.Model):
    name = models.CharField(max_length=50, null=False)
    rate = models.IntegerField(null=False)
