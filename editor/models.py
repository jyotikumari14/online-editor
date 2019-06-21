from django.db import models
from django import forms

# Create your models here.
class fileUpload(models.Model):

	name = models.CharField(max_length=100, null=True, blank=True)
	file = models.FileField(upload_to="file/")
	content = models.TextField(blank=True)
	data = models.TextField(blank=True)
	length = models.IntegerField(default=0)

	def __str__(self):
		return self.name