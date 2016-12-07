from rest_framework import viewsets

from wishlists import models
from wishlists import serializers


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WishlistSerializer
    queryset = models.Wishlist.objects.all()


class WishlistItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WishlistItemSerializer

    def get_queryset(self):
        wishlist = models.Wishlist.objects.get(id=self.kwargs['wishlist_id'])
        return models.WishlistItem.objects.filter(wishlist=wishlist)
