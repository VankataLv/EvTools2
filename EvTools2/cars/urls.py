from django.urls import path

from EvTools2.cars.views import index

urlpatterns = (
    path('', index, name='index'),
)
