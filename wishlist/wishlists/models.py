from django.db import models


class Wishlist(models.Model):
    customer = models.IntegerField(unique=True)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.IntegerField()
