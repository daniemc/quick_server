from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Vendors as VendorsTable
from api.serializers import VendorsSerializer


def get_object(id):
    try:
        return VendorsTable.objects.get(id=id)
    except VendorsTable.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class Vendors(APIView):

    def get(self, request):
        vendors = VendorsTable.objects.all()
        serializedData = VendorsSerializer(vendors, many=True)
        return Response(serializedData.data)


    def post(self, request):
        serializer = VendorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorsModification(APIView):

    def put(self, request, id):
        vendor = get_object(id=id)
        serializer = VendorsSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        vendor = get_object(id=id)
        vendor.delete()
        return Response(status=status.HTTP_200_OK)
