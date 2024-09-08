from django import forms
from .models import EVCar, User, CarModel


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['banned']


class CarForm(forms.ModelForm):

    class Meta:
        model = EVCar
        fields = '__all__'


