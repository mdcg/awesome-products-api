from api.models import Basket
from api.serializers.products_serializers import ProductSerializer
from rest_framework import serializers


class BasketSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('products',)
