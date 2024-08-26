from rest_framework import serializers

from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'author_id', 'title', 'content', 'diary_date')
        read_only_fields = ('id', 'author_id')
    
    def save(self, **kwargs):
        diary = self.context['diary']
        keys = self.validated_data.keys()
        
        if 'title'      in keys: diary.title      = self.validated_data['title']
        if 'content'    in keys: diary.content    = self.validated_data['content']
        if 'diary_date' in keys: diary.diary_date = self.validated_data['diary_date']
        
        diary.save()
        return diary


class DiaryRegistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = ('title', 'content', 'diary_date')

    def save(self, **kwargs):
        diary = Diary.objects.create(author=self.context['author'], **self.validated_data)
        return diary
