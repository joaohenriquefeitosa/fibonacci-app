from django.urls import path
from .views import fibonacci

urlpatterns = [
    path('', fibonacci),
]