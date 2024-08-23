from rest_framework import serializers

from models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'author', 'title', 'content', 'diary_date', 'updated_at')
        read_only_fields = ('id',)
