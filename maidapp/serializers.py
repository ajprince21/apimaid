from rest_framework import serializers

class MaidUserProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
    mobile_number = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=200)
