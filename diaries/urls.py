from django.urls import path

from .views import DiaryView, DiaryRegistView

urlpatterns = [
    path('', DiaryView.as_view(), name='list'),
    path('write/', DiaryRegistView.as_view(), name='write')
]
