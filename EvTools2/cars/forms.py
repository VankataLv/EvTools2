from django import forms
from .models import EVCar, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['banned']


class CarForm(forms.ModelForm):
    class Meta:
        model = EVCar
        fields = [
            'owner',
            'brand',
            'model',
            'trim_level',
            'year',
            'mileage',
            'asking_price',
            'battery_capacity',
            'range',
            'horsepower',
            'drivetrain',
            'body_type',
            'color',
            'doors',
            'vin',
            'description',
            'location',
        ]
