from django.db import models


class price_range(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(max_length=10, null=False)