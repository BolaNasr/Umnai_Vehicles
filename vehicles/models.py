from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
vehicle_types = (
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('Motorcycle', 'Motorcycle')
    )
class Vehicle(models.Model):
    vin = models.CharField(max_length=128, unique=True, primary_key=True)
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    seat_capacity = models.IntegerField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(1980), MaxValueValidator(2021)])
    type = models.CharField(max_length=64, choices=vehicle_types)



    def __str__(self):
        return f"Model: {self.model}, Seat Capacity: {self.seat_capacity}, Type: {self.type} ({self.year})"


class Car(Vehicle):
    roof_rack_availability = models.BooleanField(choices=BOOL_CHOICES)

    def __str__(self):
        return f"Roof Rack Availability: {self.roof_rack_availability} "


class Truck(Vehicle):
    haul_capacity = models.FloatField()

    def __str__(self):
        return f"Haul Capacity: {self.haul_capacity} "

class MotorCyclye(Vehicle):
        sidecar_availability = models.BooleanField(choices=BOOL_CHOICES)

        def __str__(self):
            return f"Sidecar Availability: {self.sidecar_availability} "

