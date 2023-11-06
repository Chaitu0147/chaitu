from django.db import models
import datetime
# Create your models here.


class ProductsList(models.Model):
    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    price = models.IntegerField(default=100)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
