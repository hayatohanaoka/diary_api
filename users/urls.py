from django.urls import path

from .views import UserProfileView, UserRegistView, UserView, UserTokenLoginView

urlpatterns = [
    path('', UserView.as_view(), name='list'),
    path('<int:id>/', UserProfileView.as_view(), name='profile'),
    path('login/', UserTokenLoginView.as_view(), name='token_login'),
    path('regist/', UserRegistView.as_view(), name='regist')
]
