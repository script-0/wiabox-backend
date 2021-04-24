from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from .serializers import NodeSerializer , CommunitySerializer
from .models import Node , Community


@api_view(['GET'])
def list_nodes(request):
    """
    List all nodes sort by last updated date
    """
    nodes = Node.objects.all().order_by('last_updated_at')
    serializer = NodeSerializer(nodes, many=True)
    return JsonResponse(serializer.data , safe=False)


@api_view(['GET'])
def list_communities(request):
    """
    List all Communities sort by last updated date
    """
    communities = Community.objects.all().order_by('last_updated_at')
    serializer = CommunitySerializer(communities, many=True)
    return JsonResponse(serializer.data , safe=False)