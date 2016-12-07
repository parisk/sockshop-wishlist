from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from wishlists import exceptions
from wishlists import models
from wishlists import serializers


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.WishlistSerializer
    queryset = models.Wishlist.objects.all()
    lookup_field = 'customer'


class WishlistItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.NamespacedWishlistItemSerializer
    lookup_field = 'product'

    def get_queryset(self):
        wishlist = models.Wishlist.objects.get(
            customer=self.kwargs['customer']
        )
        return models.WishlistItem.objects.filter(wishlist=wishlist)

    def create(self, request, customer):
        wishlist = models.Wishlist.objects.get(
            customer=self.kwargs['customer']
        )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            wishlist_item = serializer.create(serializer.data, wishlist)
        except exceptions.DuplicateProductInWishlist as e:
            response = Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
            return response

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

from wishlists import signals
