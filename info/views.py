from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'info/home.html')

def faq(request):
    return render(request, 'info/faq.html')