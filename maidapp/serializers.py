from rest_framework import serializers
from .models import MaidUserProfile

class MaidUserProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    mobile_number = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=200)
    monthly_Charge = serializers.FloatField(required = False, allow_null=True)

    def create(self, validated_data):
        return MaidUserProfile.objects.create(**validated_data)