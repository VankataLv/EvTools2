from django.urls import path
from EvTools2.cars.views import car_index, create_user, create_ev_car

urlpatterns = (
    path('', car_index, name='car index'),
    path('signup/', create_user, name='signup'),
    path('create-car/', create_ev_car, name='create ev car'),
)
