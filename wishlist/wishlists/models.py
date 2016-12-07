from django.db import models


class Wishlist(models.Model):
    customer = models.IntegerField(unique=True)

    def __unicode__(self):
        return 'Wishlist of customer #%s' % self.customer

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return '<WishlistObject: %s>' % self.__unicode__()


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.IntegerField()
