from django.shortcuts import render, redirect, HttpResponse
from .models import WineGrade, Wine, Country
from .forms import AddWine, AddWineGrade, AddCountry

# Create your views here.


def index(request):
    ctx = {
        'wines': Wine.objects.all(),
        'wine_grades': WineGrade.objects.all(),
        'countries': Country.objects.all()
    }
    return render(request, 'pages/index.html', ctx)


def wine(request, id):
    wine = Wine.objects.get(pk=id)
    if request.POST:
        form = AddWine(request.POST)
        if form.is_valid():
            wine.extract = form.cleaned_data['extract']
            wine.wine_grade = form.cleaned_data['wine_grade']
            wine.country = form.cleaned_data['country']
            wine.sweetness = form.cleaned_data['sweetness']
            wine.text = form.cleaned_data['text']
            wine.save(update_fields=['extract', 'wine_grade', 'country', 'sweetness', 'text'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AddWine()
    ctx = {
        'wine': wine,
        'form': form
    }
    return render(request, 'pages/wine.html', ctx)


def wine_grade(request, id):
    grade = WineGrade.objects.get(pk=id)
    if request.POST:
        form = AddWineGrade(request.POST)
        if form.is_valid():
            grade.title = form.cleaned_data['title']
            grade.color = form.cleaned_data['color']
            grade.text = form.cleaned_data['text']
            grade.save(update_fields=['title', 'color', 'text'])
        else:
            return HttpResponse('Форма введена с ошибкой')
    form = AddWineGrade()
    ctx = {
        'wine_grade': grade,
        'form': form
    }
    return render(request, 'pages/wine_grade.html', ctx)


def add_country(request):
    if request.POST:
        form = AddCountry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddCountry()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_country.html', ctx)


def add_wine_grade(request):
    if request.POST:
        form = AddWineGrade(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddWineGrade()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_wine_grade.html', ctx)


def add_wine(request):
    if request.POST:
        form = AddWine(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Форма введена с ошибкой')
    else:
        form = AddWine()
    ctx = {
        'form': form
    }
    return render(request, 'pages/add_wine.html', ctx)
