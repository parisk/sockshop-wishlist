from rest_framework import viewsets

from wishlists import models
from wishlists import serializers


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WishlistSerializer
    queryset = models.Wishlist.objects.all()
