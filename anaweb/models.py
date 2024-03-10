from django.db import models

# Create your models here.


class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image=models.ImageField(upload_to='media/slider/',blank=False)

def __str__(self):
    return self.title


class Ekibimiz(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=100, blank=False)
    image=models.ImageField(upload_to='media/Ekibimiz/',blank=False)

class Galeri(models.Model):
    image=models.ImageField(upload_to='media/Galeri', blank=False)