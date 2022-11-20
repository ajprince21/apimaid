from django.shortcuts import render
from .models import MaidUserProfile
from .serializers import MaidUserProfileSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class MaidListView(APIView):
    def get(self, request):
        maids = MaidUserProfile.objects.all()
        serializer = MaidUserProfileSerializer(maids, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MaidUserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MaidDetailView(APIView):

    def get_maid(self, pk):
        try:
            return MaidUserProfile.objects.get(pk=pk)
        except MaidUserProfile.DoesNotExist:
            raise Http404

    def get(self, request , pk):
        maid = self.get_maid(pk)
        serializer = MaidUserProfileSerializer(maid)
        return Response(serializer.data)

    def delete(self, request, pk):
        maid = self.get_maid(pk)
        maid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        maid = self.get_maid(pk)
        serializer = MaidUserProfileSerializer(maid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
