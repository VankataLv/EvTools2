from django.shortcuts import render, redirect

from EvTools2.cars.forms import UserForm, CarForm


def index(request):
    context = {}
    return render(request, 'cars/index.html', context)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

    else:  # request.method == 'GET':
        form = UserForm()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'cars/create_user_form.html', context)


from django.shortcuts import render, redirect
from .forms import CarForm


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
    else:  # request.method == 'GET':
        # brand_id = request.POST.get('brand_id')
        # form = CarForm(brand_id=brand_id)
        form = CarForm()

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'cars/create_car_form.html', context)





