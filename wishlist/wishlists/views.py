from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from wishlists import models
from wishlists import serializers


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WishlistSerializer
    queryset = models.Wishlist.objects.all()


class WishlistItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NamespacedWishlistItemSerializer

    def get_queryset(self):
        wishlist = models.Wishlist.objects.get(id=self.kwargs['wishlist_id'])
        return models.WishlistItem.objects.filter(wishlist=wishlist)

    def create(self, request, wishlist_id):
        wishlist = models.Wishlist.objects.get(id=self.kwargs['wishlist_id'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        wishlist_item = serializer.create(serializer.data, wishlist)
        headers = self.get_success_headers(serializer.data)

        response_serializer = serializers.WishlistItemSerializer(
            wishlist_item, context={
                'request': request
            }
        )
        response = Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
        return response
