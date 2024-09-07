from django.urls import path

from EvTools2.common.views import index

urlpatterns = (
    path('', index, name='index')
)