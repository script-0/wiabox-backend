from django.shortcuts import render
from rest_framework import viewsets
import json

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt

from .serializers import CommunityUserSerializer , NodeSerializer , CommunitySerializer, UserSerializer, ArticleSerializer, ServiceSerializer, DonationSerializer, EventSerializer
from .models import * 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class CommunityUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = CommunityUser.objects.all().order_by('last_updated_at')
    serializer_class = CommunityUserSerializer

class NodeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Node.objects.all().order_by('last_updated_at')
    serializer_class = NodeSerializer

class CommunityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Community.objects.all().order_by('last_updated_at')
    serializer_class = CommunitySerializer

'''
{ "id",
 "password",
 "last_login": "2021-04-25T00:01:41.396811Z", 
 "is_superuser", 
 "username",
 "first_name", 
 "last_name", 
 "email",
 "is_staff", 
 "is_active", 
 "date_joined", 
 "groups" : [], 
 "user_permissions"
}
'''
@csrf_exempt
@action(detail=False)
def list_platform(request):
    if request.method == "GET" :
        users =  User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    else :
        return JsonResponse({"error" : status.HTTP_401_UNAUTHORIZED , "description" : "Bad Request. Waiting for GET Request"}, safe=False)

@csrf_exempt
@action(detail=False)
def get_platform(request):
    if request.method == "POST" :
        data =json.loads(request.body)
        #return JsonResponse(make_password(data['key']) , safe=False)
        user = User.objects.filter(username=data['name'])
        if not user :
            return JsonResponse({"error" : status.HTTP_401_UNAUTHORIZED , "description" : "No User found with this credentials"}, safe=False)
        else:
            if( check_password(data['key'] , user[0].password) ) :
                user[0].password = data['key']
                serializer = UserSerializer(user, many=True)
                return JsonResponse(serializer.data, safe=False)
            else :
                return JsonResponse({"error" : status.HTTP_401_UNAUTHORIZED , "description" : "Bad User's credentials"}, safe=False)
    else :
        return JsonResponse({"error" : status.HTTP_401_UNAUTHORIZED , "description" : "Bad Request. Waiting for POST Request"}, safe=False)

@action(methods=['post'], detail=False)
def login(request):
    data = {
        "id" : 1,
        "username" : request.data["username"],
        "password" : request.data["password"]
    }
    refresh = RefreshToken.for_user(data)
    payload = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return JsonResponse(payload, safe=False)

@action(methods=['post'], detail=False)
def logout(request):
    platform = Platform.objects.all()
    serializer = PlatformSerializer(platform, many=True)
    return JsonResponse(serializer.data, safe=False)

@action(methods=['post'], detail=False)
def authentificate(request):
    platform = Platform.objects.all()
    serializer = PlatformSerializer(platform, many=True)
    return JsonResponse(serializer.data, safe=False)

@action(methods=['GET'], detail=False)
def retrieve(request, pk=None):
    return Response("Retrieve root : Unimplemented")

class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Article.objects.all().order_by('last_updated_at')
    serializer_class = ArticleSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Service.objects.all().order_by('last_updated_at')
    serializer_class = ServiceSerializer

class DonationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Donation.objects.all().order_by('last_updated_at')
    serializer_class = DonationSerializer

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().order_by('last_updated_at')
    serializer_class = EventSerializer