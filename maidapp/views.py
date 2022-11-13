from django.shortcuts import render
from django.http import JsonResponse
from .models import MaidUserProfile
from .serializers import MaidUserProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def maidListView(request):
    if request.method == 'GET':
        maids = MaidUserProfile.objects.all()
        serializer = MaidUserProfileSerializer(maids, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        serializer = MaidUserProfileSerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)