from django import forms
from .models import EVCar, User, CarModel


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['banned']



class CarForm(forms.ModelForm):
        # if brand_id:
        #     self.fields['model'].queryset = CarModel.objects.filter(brand_id=brand_id)

    class Meta:
        model = EVCar
        fields = '__all__'
