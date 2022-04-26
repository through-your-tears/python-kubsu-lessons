from django.shortcuts import render
from .models import WineGrade, Wine, Sweetness, Country

# Create your views here.


def index(request):
    ctx = {
        'wines': Wine.objects.all()
    }
    return render(request, 'pages/index.html', ctx)


def wine(request, id):
    ctx = {
        'wine': Wine.objects.filter(pk=id)
    }
    return render(request, 'pages/wine.html', ctx)
