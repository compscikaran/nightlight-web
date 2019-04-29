from django.shortcuts import render, redirect
from .models import ImageModel
from django.utils import timezone
from django.http import JsonResponse
import asyncio
# Create your views here.

def upload(request):
	if request.method == 'GET':
		return render(request, 'transform/upload.html')
	elif request.method == 'POST':
		if request.FILES.get('image', None) is not None:
			imodel = ImageModel()
			imodel.image = request.FILES['image']
			imodel.timestamp = timezone.datetime.now()
			imodel.save()
			return render(request, 'transform/generating.html', {'img': imodel})
		else:
			return render(request, 'transform/upload.html', {'error': 'Please provide a valid image'})
		return render(request, 'transform/generating.html')


def run_image(request):
	if request.method == 'GET':
		filename = request.headers['Filename']
		cnn(filename)
		return JsonResponse({'msg': 'success'})


def cnn(filename):
	print('Deep Learning ... on ' + str(filename))

def preview(request):
	filename = request.GET['filename']
	return render(request, 'transform/preview.html', {'filename': filename})