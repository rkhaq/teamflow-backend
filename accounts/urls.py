# accounts/urls.py
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustomTokenObtainPairView, UserRegistrationView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/auth/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google-auth/', include('allauth.urls')),
]
