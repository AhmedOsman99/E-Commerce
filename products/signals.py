from django.dispatch import Signal, receiver
from .models import Product

products_limit = Signal()

@receiver(products_limit)
def set_products_limit(sender, Category_id, **kwargs):
    no_of_products = Product.objects.filter(Category_id=Category_id).count()
    if no_of_products >= 5:
        return True
    return False