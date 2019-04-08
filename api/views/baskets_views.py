from api.models import Basket, Product
from api.serializers.baskets_serializers import BasketSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserBasketView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request, format=None):
        user_basket = request.user.basket
        serialized_basket = BasketSerializer(user_basket)

        response_data = {
            'status': 'success',
            'data': {
                'basket': serialized_basket.data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)


class UserBasketProductsView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, product_id, format=None):
        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'data': None
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        user_basket = request.user.basket
        user_basket.products.add(product)
        user_basket.save()

        serialized_basket = BasketSerializer(user_basket)

        response_data = {
            'status': 'success',
            'data': {
                'basket': serialized_basket.data
            }
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    def delete(self, request, product_id, format=None):
        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'data': None
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        user_basket = request.user.basket
        user_basket.products.remove(product)
        user_basket.save()

        serialized_basket = BasketSerializer(user_basket)

        response_data = {
            'status': 'success',
            'data': {
                'basket': serialized_basket.data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)
