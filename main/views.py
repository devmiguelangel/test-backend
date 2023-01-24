
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Serializers
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer
# Services
from .services import get_categories, create_category, get_products, create_product


class CategoryAPIView(APIView):
    def get(self, request):
        # Getting the categories from the database and serializing them
        categories = get_categories()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        # Validating the data that is being sent to the API
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Getting the validated data from the serializer
        data = serializer.validated_data
        # Create new category
        category = create_category(data)

        # Checks if the category is created
        if category:
            category_serializer = CategorySerializer(category)

            return Response(category_serializer.data)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)

class ProductAPIView(APIView):
    def get(self, request):
        # Getting the products from the database and serializing them
        products = get_products()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):
        # Validating the data that is being sent to the API
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Getting the validated data from the serializer
        data = serializer.validated_data
        # Create new product
        product = create_product(data)

        # Checks if the product is created
        if product:
            product_serializer = ProductSerializer(product)

            return Response(product_serializer.data, status=status.HTTP_201_CREATED)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)
