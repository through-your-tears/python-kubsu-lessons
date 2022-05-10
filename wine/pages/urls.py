from django.urls import path
from . import views


appname = 'pages'
urlpatterns = [
    path('', views.index, name='home'),
    path('wine/<int:id>', views.wine, name='wine'),
    path('add_wine', views.add_wine, name='add_wine'),
    path('add_country', views.add_country, name='add_country'),
    path('add_wine_grade', views.add_wine_grade, name='add_wine_grade'),
    path('wine_grade/<int:id>', views.wine_grade, name='wine_grade')
]
