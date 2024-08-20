from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    edad = models.PositiveIntegerField(null=True)
    ubicacion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)


class post(models.Model):
    descripcion= models.CharField(max_length=50)
    imagen = models.CharField(max_length=50)

