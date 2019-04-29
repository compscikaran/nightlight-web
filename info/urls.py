from django.urls import path
from .views import home, faq

urlpatterns = [
    path('', home, name='home'),
    path('faq/', faq, name='faq')
]
