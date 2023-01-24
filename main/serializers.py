from rest_framework import serializers
# Models
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """ Product serializer """

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(ProductSerializer):
    """ Product create serializer """

    category = serializers.IntegerField()


class EditProductSerializer(CreateProductSerializer):
    """ Product edit serializer """

    pass
