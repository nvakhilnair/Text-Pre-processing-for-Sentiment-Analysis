from .views import API
from django.urls import path


urlpatterns = [
    path('', API.as_view()),
    
]
