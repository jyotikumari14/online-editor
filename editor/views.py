from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
import docx2txt
import docx
from django.http import HttpResponse
from django.conf import settings
import chardet
import requests
import re

# Create your views here.

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

def readFile(request):
	doc = fileUpload.objects.last()
	my_text = docx2txt.process(settings.BASE_DIR+doc.file.url)
	nw = reptext(my_text)

	return HttpResponse(nw)

def update(request,pk):
	doc = fileUpload.objects.get(pk=pk)
	my_text = docx2txt.process(settings.BASE_DIR+doc.file.url)
	data = reptext(my_text)

	data = data.replace('\n\n','\n')
	data = data.replace('\n\n','\n')
	data = data.replace('\n','</br>')
	data = data.replace('#$#$','<input type="text">')

	return render(request,'update.html',{'data':data})
	# return HttpResponse(nw)

def fileedit(request):

	doc = fileUpload.objects.last()
	path = settings.BASE_DIR+doc.file.url
	# days_file = open(path,'r')
	days_file = open(path,'r',encoding = "ISO-8859-1")
	days = days_file.read()
	# print(days)
	for lines in open(path,'rb'):
		decodedLine = lines.decode('ISO-8859-1')
		line = decodedLine.split('\t')
		print(line)
		for decodedLine in open(path, 'r',encoding='utf-8'):
			line = decodedLine.split('\t')
			print(line)

	# complete html of site
	# r = requests.get("http://itzmejyoti.com")
	# print(r.encoding)
	# # UTF-8
	# print(type(r.text))
	# # <class 'str'>
	# print(r.text)

	# read and write file

	# path = '/Users/subhashchandra/Downloads/myfile.docx'
	# # days_file = open(path,'r')
	# days_file = open(path,'r',encoding = "ISO-8859-1")
	# days = days_file.read().decode('utf8')
	# print(days)


	# new_path = '/Users/subhashchandra/Downloads/myfile.docx'
	# new_days = open(new_path,'w')

	# title = 'Days of the Week\n'
	# new_days.write(title)
	# print(title)

	# new_days.write(days)
	# print(days)

	# days_file.close()
	# new_days.close()
	return HttpResponse("Success")

class fileUploading(viewsets.ModelViewSet):
	queryset= fileUpload.objects.all()
	serializer_class= FileSerializer
