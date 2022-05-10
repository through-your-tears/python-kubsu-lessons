from django.db import models

# Create your models here.


class Sweetness(models.Model):

    class Meta:
        verbose_name = 'Сладость вина'
        verbose_name_plural = 'Сладости вина'

    sweetness_name = models.CharField(max_length=20, verbose_name='Сладость')

    def __str__(self):
        return self.sweetness_name


class WineGrade(models.Model):

    class Meta:
        verbose_name = 'Сорт вина'
        verbose_name_plural = 'Сорта вина'

    choices = [
        (0, 'Белое'),
        (1, 'Красное')
    ]
    title = models.CharField(max_length=20, unique=True, verbose_name='Название сорта')
    color = models.IntegerField(choices=choices, verbose_name='Цвет вина')
    text = models.TextField(verbose_name='Описание сорта')

    def __str__(self):
        return self.title


class Country(models.Model):

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    title = models.CharField(max_length=30, unique=True, verbose_name='Название страны')

    def __str__(self):
        return self.title


class Wine(models.Model):

    class Meta:
        verbose_name = 'Вино'
        verbose_name_plural = 'Вина'

    extract = models.IntegerField(verbose_name='Выдержка(в годах)')
    text = models.TextField(verbose_name='Описание самого вина')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    sweetness = models.ForeignKey(Sweetness, on_delete=models.SET_NULL, null=True)
    wine_grade = models.ForeignKey(WineGrade, on_delete=models.CASCADE)
