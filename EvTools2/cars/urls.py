from django.urls import path

from EvTools2.cars.views import car_index, create_user, create_car

urlpatterns = (
    path('', car_index, name='car index'),
    path('signup/', create_user, name='signup'),
    path('create-car/', create_car, name='create car'),
)
