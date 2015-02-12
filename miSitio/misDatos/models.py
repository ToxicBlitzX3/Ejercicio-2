from django.db import models

# Create your models here.
class MisDatos(models.Model):
	nombre = models.CharField(max_length=30)
	skills = models.TextField()
	telefono = models.IntegerField()
	email = models.EmailField()
	imagen = models.FileField()
#class Social(models.Model):
	facebook = models.CharField(max_length=30)
	youtube = models.CharField(max_length=30)
	twitter = models.CharField(max_length=30)
