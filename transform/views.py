from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'transform/home.html')

def faq(request):
    return render(request, 'transform/faq.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'transform/upload.html')