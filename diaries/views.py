from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

from .models import Diary
from .serializers import DiarySerializer
from users.models import CustomUser

# Create your views here.
class DiaryView(APIView):
    def get(self, req):
        query_set = Diary.objects.filter(user=req.user)
        serializer = DiarySerializer(query_set, many=True)
        return Response(serializer.data)

class DiaryRegistView(APIView):
    def post(self, req):
        user = CustomUser.objects.filter(pk=1)
        print(user.keys())
        req.data['author'] = user
        serializer = DiarySerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(status=400)
