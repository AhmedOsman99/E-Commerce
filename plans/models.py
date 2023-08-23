from django.db import models

# Create your models here.
class Plan(models.Model):
    label = models.CharField(max_length=100)
    no_of_products = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()


class CustomPlan(models.Model):
    # label = models.CharField(max_length=100)
    no_of_products = models.IntegerField()
    storage = models.IntegerField()

    # @property
    # def calculate_price(self):
    #     x = (self.no_of_products * 0.11) + (self.storage * 0.2) + 5
    #     price = x * 31 * 12
    #     return price