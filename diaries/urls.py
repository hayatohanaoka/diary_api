from django.urls import path

from .views import DiaryView

urlpatterns = [
    path('', DiaryView.as_view(), name='list'),
]
