from django.db import models

from customers.models import Customer
from products.models import Product


class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
