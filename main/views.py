
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Serializers
from .serializers import CategorySerializer, ProductSerializer, CreateProductSerializer, EditProductSerializer
# Services
from .services import (
    get_categories, create_category, get_products, get_product, create_product, edit_product, delete_product
)


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


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        # Getting the product from the database using the primary key
        product = get_product(pk)

        # Checking if the product exists in the database
        if product:
            serializer = ProductSerializer(product)

            return Response(serializer.data)

        return Response(None, status=status.HTTP_404_NOT_FOUND)

    # Creating a new product.
    def put(self, request, pk):
        # Validating the data that is being sent to the API
        serializer = EditProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Getting the validated data from the serializer
        data = serializer.validated_data
        # Create new product
        product = edit_product(pk, data)

        # Checks if the product is created
        if product:
            product_serializer = ProductSerializer(product)

            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Delete product
        product_id = delete_product(pk)

        # Checks if the product was deleted
        if product_id:
            return Response({'product_id': product_id}, status=status.HTTP_202_ACCEPTED)

        return Response(None, status=status.HTTP_400_BAD_REQUEST)
