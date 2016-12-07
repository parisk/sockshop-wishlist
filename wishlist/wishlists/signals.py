from django.db.models.signals import pre_save
from django.dispatch import receiver

from wishlists.exceptions import DuplicateProductInWishlist
from wishlists.models import Wishlist, WishlistItem


@receiver(pre_save, sender=WishlistItem)
def ensure_unique_product_in_wishlist(sender, instance, **kwargs):
    existing_items = WishlistItem.objects.filter(
        wishlist=instance.wishlist,
        product=instance.product
    )
    if len(existing_items):
        msg = 'Product #%s already exists in wishlist of customer #%s' % (
            instance.product, instance.wishlist.customer
        )
        raise DuplicateProductInWishlist(msg)
