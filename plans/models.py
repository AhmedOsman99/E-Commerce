from django.db import models

# Create your models here.
class Plan(models.Model):
    label = models.CharField(max_length=100)
    no_of_products = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()


class CustomPlan(models.Model):
    no_of_products = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()

