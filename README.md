# README #

### What is this repository for? ###

This repository was created as an interview challenge for Umnai

### Problem definition ###

Here at Umnai_Vehicles we use Django and Django Rest Framework (DRF) to implement all the APIs used by our Angular client and mobile apps. The input data for our system originates from multiple sources - either directly from user input or via external APIs.

Your mission is to create a Django app using DRF to store and retrieve Vehicles data.


### How to start ###
* Use your favorite package manager to install the requirements
    ```
    pip3 install -r requirements.txt
    ```
* Migrate database
    ```
    python3 manage.py migrate
    ```
* Create super user
    ```
    python3 manage.py createsuperuser
    ```
    follow the prompts to choose an email and password. This will be used to access the admin site
  
* Create Database in MongoDB 
  
  ```bash
  use umnai_vehicles
  ```
  
* Strat MongoDB server
  run bash
  ```bash
  mongod
  ```
* Run django server locally
    ```bash
    python3 manage.py runserver
    ```
    Note: you might need to create super user

* Run the tests ( unitTest and end to end test.)
  
  **Note:** Need to run server before test because end to end test using actual server
    ```commandline
    python3 manage.py test
    ```

### API Options
# Vehicles
```json
URL: /vehicles/v1/vehicles/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "cars": [
        {
            "vin": "1NXBU40E29Z040601",
            "make": "Malta",
            "model": "Audi",
            "seat_capacity": 4,
            "year": 2020,
            "type": "Car",
            "roof_rack_availability": true
        }
    ],
    "trucks": [],
    "motors": [
        {
            "vin": "1NXBU40E29Z040658",
            "make": "Spain",
            "model": "M",
            "seat_capacity": 4,
            "year": 2001,
            "type": "Motorcycle",
            "sidecar_availability": true
        },
        {
            "vin": "1NXBU40E29Z040602",
            "make": "Spain",
            "model": "KIA",
            "seat_capacity": 4,
            "year": 1999,
            "type": "Motorcycle",
            "sidecar_availability": true
        }
    ]
}

```
    
```json
URL: /vehicles/v1/motor/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "vin": "1NXBU40E29Z040658",
        "make": "Spain",
        "model": "M",
        "seat_capacity": 4,
        "year": 2001,
        "type": "Motorcycle",
        "sidecar_availability": true
    },
    {
        "vin": "1NXBU40E29Z040602",
        "make": "Spain",
        "model": "KIA",
        "seat_capacity": 4,
        "year": 1999,
        "type": "Motorcycle",
        "sidecar_availability": true
    }
]
```
```json
URL: /vehicles/v1/cars/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "vin": "1NXBU40E29Z040601",
        "make": "Malta",
        "model": "Audi",
        "seat_capacity": 4,
        "year": 2020,
        "type": "Car",
        "roof_rack_availability": true
    }
]

```

```json
URL: /vehicles/v1/truck/

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[]
```

```json
URL: /vehicles/v1/vehicles/?type=car

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "cars": [
        {
            "vin": "1NXBU40E29Z040601",
            "make": "Malta",
            "model": "Audi",
            "seat_capacity": 4,
            "year": 2020,
            "type": "Car",
            "roof_rack_availability": true
        }
    ],
    "trucks": [],
    "motors": []
}

```
```json
URL: /vehicles/v1/vehicles/?make=Spain

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "cars": [],
    "trucks": [],
    "motors": [
        {
            "vin": "1NXBU40E29Z040658",
            "make": "Spain",
            "model": "M",
            "seat_capacity": 4,
            "year": 2001,
            "type": "Motorcycle",
            "sidecar_availability": true
        },
        {
            "vin": "1NXBU40E29Z040602",
            "make": "Spain",
            "model": "KIA",
            "seat_capacity": 4,
            "year": 1999,
            "type": "Motorcycle",
            "sidecar_availability": true
        }
    ]
}

```