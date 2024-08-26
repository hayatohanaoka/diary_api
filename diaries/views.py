from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Diary
from .serializers import DiarySerializer, DiaryRegistSerializer

# Create your views here.
class DiaryView(APIView):
    def get(self, req):
        query_set = Diary.objects.all()
        serializer = DiarySerializer(query_set, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = DiaryRegistSerializer(data=req.data, context={'author': req.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(status=400)


class DiaryDetailView(APIView):
    
    query_set = Diary.objects.all()
    serializer_class =DiarySerializer
    
    def get(self, req, diary_id):
        diary = get_object_or_404(self.query_set, pk=diary_id)
        serializer = self.serializer_class(diary)
        return Response(serializer.data)
    
    def patch(self, req, diary_id):
        if req.user:
            diary = get_object_or_404(self.query_set, pk=diary_id)
            
            if req.user != diary.author:
                return Response(status=404)
            
            serializer = self.serializer_class(
                data=req.data, context={'diary': diary})
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=203)
            
            return Response(status=400)
        return Response(status=403)
    
    def delete(self, req, diary_id):
        diary = get_object_or_404(self.query_set, pk=diary_id)
        
        if req.user == diary.author:
            diary.delete()
            return Response(status=204)
        
        return Response(status=403)
