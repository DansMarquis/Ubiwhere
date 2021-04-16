from django.urls import path
from .views import LoginView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='access_for_token'),
    path('register/', RegisterView.as_view(), name='register'),
]

