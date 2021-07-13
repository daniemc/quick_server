from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.serializers import ProductsSerializer


def get_object(id):
    try:
        return Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class Products(APIView):

    def get(self, request):
        products = Product.objects.all()
        print(products)
        serializedData = ProductsSerializer(products, many=True)
        return Response(serializedData.data)

        # return Response(queryset)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsModification(APIView):

    def put(self, request, id):
        measure = get_object(id=id)
        serializer = ProductsSerializer(measure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        measure = get_object(id=id)
        measure.delete()
        return Response(status=status.HTTP_200_OK)