from django.shortcuts import render, redirect
from EvTools2.cars.forms import UserForm, CarForm
from EvTools2.cars.models import EVCar


def index(request):
    cars = EVCar.objects.all()
    context = {'cars': cars, }
    return render(request, 'cars/car_index.html', context)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:  # request.method == 'GET':
        form = UserForm()

    context = {'form': form}
    return render(request, 'cars/create_user_form.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:  # request.method == 'GET':
        form = CarForm()

    context = {'form': form}
    return render(request, 'cars/create_car_form.html', context)

