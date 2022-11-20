from rest_framework import serializers
from .models import MaidUserProfile
from django.contrib.auth.models import User

class MaidUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaidUserProfile
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'