from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import NodeSerializer , CommunitySerializer
from .models import Node , Community

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all().order_by('last_updated_at')
    serializer_class = NodeSerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all().order_by('last_updated_at')
    serializer_class = CommunitySerializer
