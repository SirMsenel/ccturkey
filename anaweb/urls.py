from django.urls import path,include
from . import views
from .views import authView, home, Anasayfa

app_name = 'anaweb'

urlpatterns = [
    path("",include("django.contrib.auth.urls")),
    path("",views.home, name='home' ),
    path("Anasayfa/",views.Anasayfa, name='Anasayfa'),
    path("signup/", authView, name="authView"),

]