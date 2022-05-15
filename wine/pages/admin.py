from django.contrib import admin
from .models import Sweetness, Wine, WineGrade, Country, Color

# Register your models here.

admin.site.register(Country)
admin.site.register(Sweetness)
admin.site.register(Wine)
admin.site.register(WineGrade)
admin.site.register(Color)
