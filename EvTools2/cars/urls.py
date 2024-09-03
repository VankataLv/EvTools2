from django.urls import path

from EvTools2.cars.views import index, create_user, create_car

urlpatterns = (
    # path('', index, name='index'),
    path('signup/', create_user, name='signup'),
    path('create-car/', create_car, name='create car'),
)
