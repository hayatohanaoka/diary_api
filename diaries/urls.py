from django.urls import path

from .views import DiaryView, DiaryDetailView

urlpatterns = [
    path('', DiaryView.as_view(), name='list'),
    path('<str:diary_id>/details/', DiaryDetailView.as_view(), name='detail')
]
