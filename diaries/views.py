from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from .models import Diary
from .serializers import DiarySerializer, DiaryRegistSerializer

# Create your views here.
class DiaryView(APIView):
    def get(self, req):
        query_set = Diary.objects.filter(user=req.user)
        serializer = DiarySerializer(query_set, many=True)
        return Response(serializer.data)
    
    def post(self, req):
        serializer = DiaryRegistSerializer(data=req.data, context={'author': req.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(status=400)
