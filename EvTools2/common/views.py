from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'common/index.html', context)


def under_construction(request):
    context = {}
    return render(request, 'common/under-construction.html', context)
