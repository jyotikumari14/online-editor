from rest_framework import serializers
from django.conf import settings
import docx2txt
from .models import *

def reptext(text):
	print("")
	try:
		text = text.replace('___','#$#$')
	except Exception as e:
		pass

	try:
		text = text.replace('#$#$_','')
		text = reptext(text)
	except Exception as e:
		pass

	try:
		text = text.replace('#$#$#$#$','#$#$')
		# text = reptext(text)
	except Exception as e:
		pass
	return text

class FileSerializer(serializers.ModelSerializer):
	
	detail = serializers.SerializerMethodField('details')
	class Meta:
		model = fileUpload
		fields= '__all__'

	def details(self,obj):
		return reptext(docx2txt.process(settings.BASE_DIR+obj.file.url))