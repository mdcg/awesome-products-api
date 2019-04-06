from api.serializers.products_serializers import ProductSerializer
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
