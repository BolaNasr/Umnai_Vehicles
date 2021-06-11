import requests

from django.test import TestCase
from rest_framework import status
from vehicles.constants import *

class VehicleViewTestCase(TestCase):
    base_url = "http://localhost:3390/vehicles/v1/"
    MAKES = ["Sweden", "Malta", "Egypt", "Poland"]
    MODELS = ["Audi", "BMW", "Hundai"]
    VINS = ["1HGCG1657WA051534", "TRUSC28N341016582", "1G8ZH1277XZ105148", "1G8ZH1277XZ105158"]
    CAPACITY = [4, 2, 10, 5]
    DATES = [2020, 1998, 1990, 1994]

    data_car1 = {
        VIN: VINS[0],
        MAKE: MAKES[0],
        SEAT_CAPACITY: CAPACITY[0],
        YEAR: DATES[0],
        TYPE: "Car",
        MODEL: MODELS[0],
        ROOF_RACK_AVAILABILITY: True
    }

    data_car2 = {
        VIN: VINS[1],
        MAKE: MAKES[1],
        SEAT_CAPACITY: CAPACITY[1],
        YEAR: DATES[1],
        TYPE: "Car",
        MODEL: MODELS[1],
        ROOF_RACK_AVAILABILITY: True
    }

    data_car3 = {
        VIN: VINS[2],
        MAKE: MAKES[2],
        SEAT_CAPACITY: CAPACITY[2],
        YEAR: DATES[2],
        TYPE: "Car",
        MODEL: MODELS[2],
        ROOF_RACK_AVAILABILITY: True
    }

    data_truck = {
        VIN: VINS[0],
        MAKE: MAKES[2],
        SEAT_CAPACITY: CAPACITY[2],
        YEAR: DATES[2],
        TYPE: "Truck",
        MODEL: MODELS[0],
        HAUL_CAPACITY: 4
    }

    update_car = {
        VIN: VINS[2],
        MAKE: MAKES[1],
        SEAT_CAPACITY: CAPACITY[2],
        YEAR: DATES[2],
        TYPE: "Car",
        MODEL: MODELS[2],
        ROOF_RACK_AVAILABILITY: True
    }
    def test_create_update_filter_delete_vehicles(self):
        session = requests.Session()

        response = session.post(self.base_url + 'cars/', json=self.data_car1, timeout=2.0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("=======Created First Car ========")

        response = session.post(self.base_url + 'cars/', json=self.data_car1, timeout=2.0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("=======Cant create any vehicles with the same vin  ========")


        response = session.post(self.base_url + 'cars/', json=self.data_car2, timeout=2.0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("=======Created Second Car ========")

        response = session.post(self.base_url + 'cars/', json=self.data_car3, timeout=2.0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("=======Created Third Car ========")

        response = session.post(self.base_url + 'truck/', json=self.data_truck, timeout=2.0)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("=======Cant create Truck  with the same Vin of car  ========")

        print("=======get specific type of vehicles ========")
        response = session.get(self.base_url + 'vehicles?type=Car', json=self.data_car3, timeout=2.0)
        self.assertEqual(len(response.json()), 3)

        print("=======get specific all vehicles with specific make ========")
        response = session.get(self.base_url + 'vehicles?make=egypt', json=self.data_car3, timeout=2.0)
        self.assertEqual(len(response.json()["cars"]), 0)

        print("=======get specific all vehicles with specific vin ========")
        response = session.get(self.base_url + 'vehicles?vin=TRUSC28N341016582', json=self.data_car3, timeout=2.0)
        self.assertEqual(len(response.json()["cars"]), 1)

        print("=======Update the Car ========")
        requests.put(self.base_url + f'cars/{self.VINS[2]}', json=self.update_car, timeout=2.0)

        print("=======check if car updated ========")
        response = session.get(self.base_url + f'vehicles?make={self.MAKES[1]}', json=self.data_car3, timeout=2.0)
        self.assertEqual(len(response.json()["cars"]), 2)

        session.delete(self.base_url + f'cars/{self.VINS[0]}', timeout=2.0)
        print("=======Deleted First Car ========")
        session.delete(self.base_url + f'cars/{self.VINS[1]}', timeout = 2.0)
        print("=======Deleted Second Car ========")
        session.delete(self.base_url + f'cars/{self.VINS[2]}', timeout = 2.0)
        print("=======Deleted Third Car ========")


        print("                        \o/")
        print("End To End test Success  | ")
        print("                        / \\")


