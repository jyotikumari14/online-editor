from rest_framework import serializers
from django.conf import settings
import docx2txt
import json
import re
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
	html = serializers.SerializerMethodField('hdata')
	data = serializers.SerializerMethodField('fdata')
	class Meta:
		model = fileUpload
		fields= '__all__'

	def fdata(self,obj):
		data = obj.data
		if obj.data:
			data = json.loads(obj.data)
		return data

	def details(self,obj):
		data = reptext(docx2txt.process(settings.BASE_DIR+obj.file.url))
		data = data.replace('\n \n','\n')
		data = re.sub(r'\n+', '\n', data).strip()
		return data

	def hdata(self,obj):
		data = reptext(docx2txt.process(settings.BASE_DIR+obj.file.url))
		data = data.replace('\n \n','\n')
		data = re.sub(r'\n+', '\n', data).strip()
		data = data.replace('\n','</br>')
		data = data.replace('#$#$','<input type="text" name="content[]" value="">')
		if obj.data:
			dfrm = json.loads(obj.data)
			for val in dfrm:
				data = data.replace('value=""', 'value="'+val+'"',1)

		return data
