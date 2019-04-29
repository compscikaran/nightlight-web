from django.shortcuts import render

# Create your views here.

def upload(request):
	if request.method == 'GET':
		return render(request, 'transform/upload.html')
	elif request.method == 'POST':
		return render(request, 'transform/generating.html')

