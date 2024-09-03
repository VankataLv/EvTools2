from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'cars/index.html', context)