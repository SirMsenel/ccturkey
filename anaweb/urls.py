from django.urls import path
from . import views

app_name = 'anaweb'

urlpatterns = [
    path("",views.home, name='home' ),
    path("Anasayfa/",views.Anasayfa, name='Anasayfa'),
    path("Anasayfa/hakkimizda/",views.Anasayfa, name='hakkimizda')

]