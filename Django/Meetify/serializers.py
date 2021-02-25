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


class MatchesSerializerMatchedWith(serializers.ModelSerializer):
    match_id = serializers.SerializerMethodField()
    matched_with = serializers.SerializerMethodField()
    self_accepted = serializers.SerializerMethodField()
    other_accepted = serializers.SerializerMethodField()

    class Meta:
        model = Matches
        fields = ['match_id', 'matched_with', 'self_accepted', 'other_accepted']

    def get_match_id(self, obj):
        return obj.pk

    def get_matched_with(self, obj):
        if self.context.get("user_id") == obj.User1_id:
            return obj.User2_id
        return obj.User1_id

    def get_self_accepted(self, obj):
        if self.context.get("user_id") == obj.User1_id:
            return obj.AcceptedByUser1
        return obj.AcceptedByUser2

    def get_other_accepted(self, obj):
        if self.context.get("user_id") == obj.User1_id:
            return obj.AcceptedByUser2
        return obj.AcceptedByUser1


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked_Songs
        fields = '__all__'