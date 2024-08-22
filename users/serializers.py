from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'nickname')
        read_only_fields = ('id',)

class UserRegistSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'email', 'password')
    
    def save(self, **kwargs):
        user = CustomUser.objects.create_user(
            username=self.validated_data['username'],
            nickname=self.validated_data['nickname'],
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        return user

class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField()
    nickname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def save(self, **kwargs):
        user = self.context['user']
        keys = self.validated_data.keys()
        if 'username'  in keys: user.username = self.validated_data['username']
        if 'nickname'  in keys: user.nickname = self.validated_data['nickname']
        if 'email'     in keys: user.email    = self.validated_data['email']
        if 'password'  in keys: user.password = self.validated_data['password']
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        keys = data.keys()
        if 'email' in keys and 'password' in keys:
            return data
        return serializers.ValidationError('email and password is required')
