from django.urls import path
from .views import predict

urlpatterns = [
    path('chatbot-msg/', predict, name='chatbot-msg'),
    
]