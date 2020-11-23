from django.shortcuts import render


def index(request):
    return render(request, 'lazyhelper/index.html')

def catalog(request):
    return render(request, 'lazyhelper/catalog.html')