from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from .serializers import NodeSerializer , CommunitySerializer, PlatformSerializer
from .models import Node , Community , Platform

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('last_updated_at')
    serializer_class = NodeSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all().order_by('last_updated_at')
    serializer_class = CommunitySerializer

class PlatformViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return JsonResponse(serializer.data, safe=False)

    def login(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return JsonResponse(serializer.data, safe=False)


    def logout(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return JsonResponse(serializer.data, safe=False)


    def authentificate(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return JsonResponse(serializer.data, safe=False)


    def retrieve(self, request, pk=None):
        return Response("")