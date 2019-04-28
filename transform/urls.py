from django.urls import path
from .views import home, upload, faq

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload,name='upload_image'),
    path('faq/', faq, name='faq')
]
