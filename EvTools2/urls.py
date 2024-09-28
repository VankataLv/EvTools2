from django.contrib import admin
from django.urls import path, include

from EvTools2.common.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cars/', include('EvTools2.cars.urls')),
    path('common/', include('EvTools2.common.urls')),
]
