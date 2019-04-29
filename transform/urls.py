from django.urls import path
from .views import upload, run_image

urlpatterns = [
    path('generating/', run_image, name='run_image'),
    path('upload/', upload,name='upload_image'),
]
