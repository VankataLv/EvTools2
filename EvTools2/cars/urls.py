from django.urls import path

from EvTools2.cars.views import index, create_user

urlpatterns = (
    path('', index, name='index'),
    path('signup/', create_user, name='signup'),
)
