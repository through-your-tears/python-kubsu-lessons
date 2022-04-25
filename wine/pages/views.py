from django.shortcuts import render
from .models import Wine_grade, Wine, Sweetness, Country

# Create your views here.


def index(request):
    ctx = {
        'wines': Wine.objects.all()
    }
    return render(request, 'index.html', ctx)
