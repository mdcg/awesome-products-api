from api.models import Product
from api.serializers.products_serializers import ProductSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterProductView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        user = request.user
        product_to_register = ProductSerializer(data=request.data)

        if product_to_register.is_valid():
            product = product_to_register.save(user=user)
            product.user = user
            product.save()

            response_data = {
                'status': 'success',
                'message': 'Product successfully registered!',
                'data': None,
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': 'fail',
            'message': 'Something went wrong!',
            'data': product_to_register.errors,
        }

        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class ListProductsView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True)

        response_data = {
            'status': 'success',
            'message': None,
            'data': serialized_products.data
        }

        return Response(response_data, status=status.HTTP_200_OK)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            response_data = {
                'status': 'fail',
                'message': 'Product not found.',
                'data': None
            }

            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serialized_product = ProductSerializer(product)
        response_data = {
            'status': 'succcess',
            'message': None,
            'data': serialized_product.data
        }

        return Response(response_data, status=status.HTTP_200_OK)
