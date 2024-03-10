from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import slider
from .models import Ekibimiz
from .models import Galeri

# Create your views here.

@login_required
def Anasayfa(request):
    sliderdata = slider.objects.all()
    ekibimizdata = Ekibimiz.objects.all()
    Galeridata = Galeri.objects.all()
    context = {
        'slider' : sliderdata,
        'Ekibimiz' : ekibimizdata,
        'Galeri' : Galeridata
    }
    return render(request,"anasayfa.html",context)


def home(request):
    return render(request,"index.html")


def authView(request) :
    if request.method == "POST" :
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("anaweb:login")
    else:
        form = UserCreationForm()
    return render(request,"registration/signup.html",{"form" : form})
