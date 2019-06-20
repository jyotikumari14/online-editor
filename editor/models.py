from django.db import models
from django import forms

# Create your models here.
class fileUpload(models.Model):

	name = models.CharField(max_length=100)
	file = models.FileField(upload_to="file/")

	def __str__(self):
		return self.name