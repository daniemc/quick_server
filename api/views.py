from django.http import HttpResponse
from rest_framework import permissions, status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithToken, MeasuresSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UnitMeasures


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    # this is because the user would not have to be logged before for the sign up/in
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_object(id):
    try:
        return UnitMeasures.objects.get(id=id)
    except UnitMeasures.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


class Measures(APIView):

    def get(self, request, format=None):
        measures = UnitMeasures.objects.all()
        serializedData = MeasuresSerializer(measures, many=True)
        return Response(serializedData.data)

        # return Response(queryset)

    def post(self, request, format=None):
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
