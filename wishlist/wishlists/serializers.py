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
