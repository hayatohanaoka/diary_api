from django.db import models
import uuid

from users.models import CustomUser

# Create your models here.
class Diary(models.Model):
    class Meta:
        db_table = 'tbl_diaries'
    
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='ID')
    title      = models.CharField(max_length=20, blank=True, verbose_name='タイトル')
    content    = models.CharField(max_length=500, blank=True, verbose_name='本文')
    diary_date = models.DateField(blank=True, verbose_name='日付')
    created_at = models.DateField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateField(auto_now=True, verbose_name='更新日時')
    author     = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author', verbose_name='筆者')
