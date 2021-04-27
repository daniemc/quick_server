from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import UnitMeasures
from api.serializers import MeasuresSerializer


def get_object(id):
    try:
        return UnitMeasures.objects.get(id=id)
    except UnitMeasures.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class Measures(APIView):

    def get(self, request):
        measures = UnitMeasures.objects.all()
        serializedData = MeasuresSerializer(measures, many=True)
        return Response(serializedData.data)

        # return Response(queryset)

    def post(self, request):
        serializer = MeasuresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasuresModification(APIView):

    def put(self, request, id):
        measure = get_object(id=id)
        serializer = MeasuresSerializer(measure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        measure = get_object(id=id)
        measure.delete()
        return Response(status=status.HTTP_200_OK)