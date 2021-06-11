from django.urls import path,re_path
from .views import VehicleView, CarsView, TrucksView, MotorCyclyeView

urlpatterns = [
    path('vehicles/', VehicleView.as_view(), name="vehicles"),
    re_path(r'truck/(?P<vin>\w+)?', TrucksView.as_view(), name="truck"),
    re_path(r'cars/(?P<vin>\w+)?', CarsView.as_view(), name="cars"),
    re_path('motor/(?P<vin>\w+)?', MotorCyclyeView.as_view(), name="motor")
]
