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
    elif request.method == 'POST':
        print(request)
        json_data = JSONParser().parse(request)
        print(json_data)
        
        return JsonResponse({'message':'Post request'}, safe=False)