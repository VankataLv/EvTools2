from django.urls import path

from EvTools2.common.views import index, under_construction

urlpatterns = (
    path('', index, name='index'),
    path('under_construction/', under_construction, name='under construction'),
)
