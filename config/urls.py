from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    # simpleJWT
    path('api_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api_token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api_token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
