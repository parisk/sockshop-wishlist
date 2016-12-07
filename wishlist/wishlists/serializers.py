from rest_framework import serializers

from wishlists.models import Wishlist, WishlistItem


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id', 'customer')


class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ('id', 'wishlist', 'product')

class NamespacedWishlistItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishlistItem
        fields = ('id', 'product',)

    def create(self, validated_data, wishlist):
        wishlist.refresh_from_db()
        wishlist_item = WishlistItem.objects.create(
            wishlist=wishlist, **validated_data
        )

        return wishlist_item
