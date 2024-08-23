from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import auth
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import UserSerializer, UserRegistSerializer, UserUpdateSerializer, UserLoginSerializer

# Create your views here.
class UserView(APIView):

    def get(self, req):
        query_set = CustomUser.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data, status=200)

class UserProfileView(APIView):

    def get(self, req, id):
        query_set = CustomUser.objects.all()
        user = get_object_or_404(query_set, id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserRegistView(APIView):

    def post(self, req):
        serializer = UserRegistSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserUpdateView(APIView):

    def patch(self, req, id):
        serializer = UserUpdateSerializer(req.data, context={'user': req.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(status=400)

class UserTokenLoginView(APIView):

    def post(self, req):
        serializer = UserLoginSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            user = auth.authenticate(req, **serializer.validated_data)
            
            if not user or not user.is_active:
                return Response('Authorize is Failed', status=400)
            
            token = Token.objects.get_or_create(user=user)
            
            return Response({'token': token[0].key}, status=200)
        return Response(serializer.errors, status=400)
