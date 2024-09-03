from django.shortcuts import render

from EvTools2.cars.forms import UserForm


def index(request):
    context = {}
    return render(request, 'cars/index.html', context)


def create_user(request):
    if request.method == 'GET':
        form = UserForm()

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'cars/create_user_form.html', {'form': form})


