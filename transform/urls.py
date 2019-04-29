from django.urls import path
from .views import upload, run_image, preview

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('run/', run_image, name='run_image'),
    path('preview/', preview, name='preview'),
]
