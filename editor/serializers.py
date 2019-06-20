from rest_framework import serializers
from django.conf import settings
import docx2txt
from .models import *



class FileSerializer(serializers.ModelSerializer):
	
	detail = serializers.SerializerMethodField('details')
	class Meta:
		model = fileUpload
		fields= '__all__'

	def details(self,obj):
		return docx2txt.process(settings.BASE_DIR+obj.file.url)