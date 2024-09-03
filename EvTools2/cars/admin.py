from django.contrib import admin
from EvTools2.cars.models import User, CarBrand, CarModel, EVCar


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'email', 'phone_number', 'banned', 'created_on']


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name',]


@admin.register(EVCar)
class EVCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'brand', 'model', 'year', 'asking_price']