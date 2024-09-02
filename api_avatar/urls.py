from django.urls import path
from api_avatar.views import index

urlpatterns = [
    path('', index),
]