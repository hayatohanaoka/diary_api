from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import UserSerializer, UserRegistSerializer, UserUpdateSerializer, UserLoginSerializer

# Create your views here.
class UserView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    
    def get(self, req):
        query_set = CustomUser.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, req):
        serializer = UserRegistSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserProfileView(APIView):

    def get(self, req, id):
        query_set = CustomUser.objects.all()
        user = get_object_or_404(query_set, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, req, id):
        if req.user.id == id:
            serializer = UserUpdateSerializer(data=req.data, context={'user': req.user})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=200)
        return Response(status=400)
    
    def delete(self, req, id):
        if req.user.id == id:
            user = CustomUser.objects.filter(pk=id)
            user.delete()
            return Response(status=204)
        return Response(status=400)

class UserTokenLoginView(APIView):
    
    permission_classes = (permissions.AllowAny,)

    def post(self, req):
        serializer = UserLoginSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            
            user = auth.authenticate(req, **serializer.validated_data)
            
            if not user or not user.is_active:
                return Response('Authorize is Failed', status=400)
            
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=201)
        return Response(serializer.errors, status=400)

