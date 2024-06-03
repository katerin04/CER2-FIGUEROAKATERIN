from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tema = models.CharField(max_length=200)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

