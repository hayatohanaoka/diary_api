from rest_framework import serializers

from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'author', 'title', 'content', 'diary_date', 'updated_at')
        read_only_fields = ('id',)

class DiaryRegistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = ('title', 'content', 'diary_date')

    def save(self, **kwargs):
        diary = Diary.objects.create(author=self.context['author'], **self.validated_data)
        return diary
