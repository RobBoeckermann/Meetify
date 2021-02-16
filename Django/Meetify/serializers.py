from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'email', 'is_active', 'date_joined']

        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = '__all__'


class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked_Songs
        fields = '__all__'