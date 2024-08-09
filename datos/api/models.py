from django.db import models

class usuarios(models.Model):
  nombre = models.CharField(max_length=50)
  apellidos = models.CharField(max_length=50)
  edad = models.IntegerField()
  telefono = models.IntegerField()
  ubicacion = models.CharField(max_length=50)
  correo = models.CharField(max_length=50)
  contrasena = models.CharField(max_length=50) 
