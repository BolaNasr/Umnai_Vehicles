from rest_framework import generics
from .serializers import VehicleSerializer, TruckSerializer, CarSerializer,MotorCyclyserializer
from .models import Vehicle, Car, MotorCyclye, Truck
from .pagination import CustomPagination
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .constants import *
class CarsView(generics.ListCreateAPIView, DestroyAPIView, UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    lookup_field = VIN
    def get_queryset(self):
        """
        fetch query_params from the request and apply filters to the query_set accordingly
        :return: the filtered query_set
        """
        query_set = self.queryset.order_by("-year")

        return query_set


class TrucksView(generics.ListCreateAPIView,DestroyAPIView, UpdateAPIView):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
    lookup_field = VIN
    def get_queryset(self):
        """
        fetch query_params from the request and apply filters to the query_set accordingly
        :return: the filtered query_set
        """
        query_set = self.queryset.order_by("-year")

        return query_set

class MotorCyclyeView(generics.ListCreateAPIView, DestroyAPIView, UpdateAPIView):
    serializer_class = MotorCyclyserializer
    queryset = MotorCyclye.objects.all()
    lookup_field = VIN
    def get_queryset(self):
        """
        fetch query_params from the request and apply filters to the query_set accordingly
        :return: the filtered query_set
        """
        query_set = self.queryset.order_by("-year")

        return query_set


class VehicleView(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer
    pagination_class = CustomPagination
    queryset = Vehicle.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VehicleSerializer(queryset, request=request, many=True)
        return Response(serializer.data[0])

