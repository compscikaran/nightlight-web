from django.shortcuts import render
from .models import ImageModel
from django.utils import timezone
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
			return render(request, 'transform/generating.html')
		else:
			return render(request, 'transform/upload.html', {'error': 'Please provide a valid image'})
		return render(request, 'transform/generating.html')

