from rest_framework import serializers
from .models import Car, MotorCyclye, Truck
from .constants import *

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        proxy = True
        fields = '__all__'
        order_by = ['-year']


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        proxy = True
        fields = '__all__'
        order_by = ['-year']

class MotorCyclyserializer(serializers.ModelSerializer):
    class Meta:
        model = MotorCyclye
        proxy = True
        fields = '__all__'
        order_by = ['-year']

class VehicleSerializer(serializers.Serializer):
    cars = serializers.SerializerMethodField('get_cars')
    trucks = serializers.SerializerMethodField('get_trucks')
    motors = serializers.SerializerMethodField('get_motors')

    def __init__(self, *args, **kwargs):
        if "request" in kwargs:
            request = kwargs.pop("request")
            self.vin = request.query_params.get(VIN, None)
            self.make = request.query_params.get(MAKE, None)
            self.type = request.query_params.get(TYPE, None)
        super(VehicleSerializer, self).__init__(*args, **kwargs)

    def get_filter(self, queryset):
        """
        filter all vehcile depend on params
        """
        if self.vin:
            queryset = queryset.filter(vin__exact=self.vin)
        if self.make:
            queryset = queryset.filter(make__exact=self.make)
        if self.type:
            queryset = queryset.filter(type__exact=self.type.capitalize())
        return queryset

    def get_cars(self, obj):

        return CarSerializer(self.get_filter(Car.objects.all()).order_by("-year"), many=True).data

    def get_trucks(self, obj):

        return TruckSerializer(self.get_filter(Truck.objects.all()).order_by("-year"), many=True).data

    def get_motors(self, obj):

        return MotorCyclyserializer(self.get_filter(MotorCyclye.objects.all()).order_by("-year"), many=True).data


