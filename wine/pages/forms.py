from django.forms import models

from .models import Country, WineGrade, Wine


class AddCountry(models.ModelForm):

    class Meta:
        model = Country
        fields = ('title',)


class AddWineGrade(models.ModelForm):

    class Meta:
        model = WineGrade
        fields = ('title', 'color', 'text')


class AddWine(models.ModelForm):

    class Meta:
        model = Wine
        fields = ('text', 'extract', 'country', 'sweetness', 'wine_grade')
