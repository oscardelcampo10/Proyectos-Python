from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre= models.CharField(max_length= 50)
	apellidos= models.CharField(max_length=70)
	Edad= models.IntegerField()
	Telefono= models.CharField(max_length= 70)
	email= models.EmailField()
	Domicilio= models.TextField()
	