from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.JSONField()


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.JSONField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)