from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('wine/<int:id>', views.wine, name='wine')
]