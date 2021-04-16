from django.urls import path, include
from rest_framework import urlpatterns
from .router import router
urlpatterns = [
    path('', include(router.urls))
]