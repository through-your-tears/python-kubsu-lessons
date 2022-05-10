from django.contrib import admin
from .models import Sweetness, Wine, WineGrade, Country

# Register your models here.

admin.site.register(Country)
admin.site.register(Sweetness)
admin.site.register(Wine)
admin.site.register(WineGrade)
