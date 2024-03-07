from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Anasayfa(request):
    return render(request,"anasayfa.html")


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
