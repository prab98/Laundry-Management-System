from django.urls import path

from .views import orderrequest

urlpatterns = [
    path('', orderrequest, name='order'),
    
]