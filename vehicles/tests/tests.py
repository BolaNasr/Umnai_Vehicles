from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

from vehicles.constants import *
from vehicles.models import Car, Truck, MotorCyclye


class VehicleViewTestCase(TestCase):
    MAKES = ["Sweden", "Malta", "Egypt", "Poland"]
    MODELS = ["Audi", "BMW", "Hundai"]
    VINS = ["1HGCG1657WA051534", "TRUSC28N341016582","1G8ZH1277XZ105148","1G8ZH1277XZ105158"]
    CAPACITY = [4, 2,10,5]
    DATES = [2020, 1998 , 1990, 1994]

    def setUp(self):
        self.client = APIClient()

    def test_create_car(self):
        """
        test creating a new car successfully
        """
        old_car_count = Car.objects.count()
        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[0],
            SEAT_CAPACITY: self.CAPACITY[0] ,
            YEAR: self.DATES[0],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: True
        }
        response = self.client.post(reverse('cars'), data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Car.objects.count(), old_car_count + 1)

    def test_create_car_invalid_year(self):
        """
        test creating a car with invalid year, should return error response with a message.
        also shouldn't create a new object
        """
        old_car_count = Car.objects.count()
        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[0],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: 2025,
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: True
        }
        response = self.client.post(reverse('cars'), data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(YEAR in response.json())
        self.assertEquals(Car.objects.count(), old_car_count)

    def test_create_car_invalid_type(self):
        """
        test creating a car with invalid type, should return error response with a message.
        also shouldn't create a new object
        """
        old_car_count = Car.objects.count()
        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[0],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: 2025,
            TYPE: "AUDI",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: True
        }
        response = self.client.post(reverse('cars'), data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(TYPE in response.json())
        self.assertEquals(Car.objects.count(), old_car_count)

    def test_get_all_cars(self):
        """
        get without query_params should return all the cars
        """
        response = self.client.get(reverse('cars'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.json()), Car.objects.count())

    def test_get_cars_filtered_by_year(self):
        """
        get all cars with filter year
        """
        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[0],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: True
        }
        self.client.post(reverse('cars'), data=data)

        response = self.client.get(reverse('cars'), data={YEAR: self.DATES[-1]})
        self.assertGreater(len(response.json()), 0)

        self.assertGreaterEqual(self.DATES[-1], response.json()[0]["year"])

    def test_get_cars_filtered_by_make(self):
        """
        get all cars with filter make
        """
        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)
        response = self.client.get(reverse('cars'), data={MAKE: self.MAKES[-1]})
        self.assertGreater(len(response.json()), 0)

        self.assertGreaterEqual(self.MAKES[-1], response.json()[0]["make"])

    def test_get_cars_filtered_by_vin(self):
        """
        get all cars with filter vin
        """
        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)
        response = self.client.get(reverse('cars'), data={VIN: self.VINS[-1]})
        self.assertGreater(len(response.json()), 0)

        self.assertGreaterEqual(self.VINS[-1], response.json()[0]["vin"])

    def test_update_car(self):
        """
        update specific car
        """
        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)
        response = self.client.get(reverse('cars'), data={VIN: self.VINS[-1]})
        self.assertGreater(len(response.json()), 0)

        self.assertGreaterEqual(self.VINS[-1], response.json()[0]["vin"])

        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.put(reverse('cars', kwargs={"vin": self.VINS[-1]}), data=data)

        response = self.client.get(reverse('cars'), data={VIN: self.VINS[-1]})
        self.assertGreater(len(response.json()), 0)

        self.assertGreaterEqual(self.MAKES[1], response.json()[0]["make"])

    def test_get_all_vehicles(self):
        """
        get without query_params should return all the vehicles
        """
        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)

        data = {
            VIN: self.VINS[0],
            MAKE: self.MAKES[2],
            SEAT_CAPACITY: self.CAPACITY[2],
            YEAR: self.DATES[2],
            TYPE: "Truck",
            MODEL: self.MODELS[0],
            HAUL_CAPACITY: 4
        }
        self.client.post(reverse('truck'), data=data)

        data = {
            VIN: self.VINS[1],
            MAKE: self.MAKES[1],
            SEAT_CAPACITY: self.CAPACITY[1],
            YEAR: self.DATES[1],
            TYPE: "Motorcycle",
            MODEL: self.MODELS[1],
            SIDECAR_AVAILABILITY: False
        }
        self.client.post(reverse('motor'), data=data)

        data = {
            VIN: self.VINS[2],
            MAKE: self.MAKES[1],
            SEAT_CAPACITY: self.CAPACITY[1],
            YEAR: self.DATES[1],
            TYPE: "Motorcycle",
            MODEL: self.MODELS[1],
            SIDECAR_AVAILABILITY: False
        }
        self.client.post(reverse('motor'), data=data)

        response = self.client.get(reverse('vehicles'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        all_vehicles = len(response.json()["motors"]) + len(response.json()["cars"]) + len(response.json()["trucks"])
        self.assertEquals(all_vehicles, Car.objects.count()+Truck.objects.count()+MotorCyclye.objects.count())

    def test_get_vehicles_filtered_by_vin(self):
        """
        get all vehicles filtered by vin
        """
        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)
        response = self.client.get(reverse('vehicles'), data={VIN: self.VINS[-1]})
        self.assertGreater(len(response.json()["cars"]), 0)
        self.assertGreaterEqual(self.VINS[-1], response.json()["cars"][0]["vin"])


    def test_get_vehicles_filtered_by_make(self):
        """
        get all vehicles filtered by make
        """
        data = {
            VIN: self.VINS[-1],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[0],
            YEAR: self.DATES[-1],
            TYPE: "Car",
            MODEL: self.MODELS[0],
            ROOF_RACK_AVAILABILITY: False
        }
        self.client.post(reverse('cars'), data=data)

        data = {
            VIN: self.VINS[2],
            MAKE: self.MAKES[-1],
            SEAT_CAPACITY: self.CAPACITY[1],
            YEAR: self.DATES[1],
            TYPE: "Motorcycle",
            MODEL: self.MODELS[1],
            SIDECAR_AVAILABILITY: False
        }
        self.client.post(reverse('motor'), data=data)

        response = self.client.get(reverse('vehicles'), data={MAKE: self.MAKES[-1]})
        self.assertGreater(len(response.json()["cars"]), 0)
        self.assertGreater(len(response.json()["motors"]), 0)
        self.assertGreaterEqual(self.MAKES[-1], response.json()["cars"][0]["make"])
        self.assertGreaterEqual(self.MAKES[-1], response.json()["motors"][0]["make"])

