from rest_framework import serializers

from .models import CommunityUser, Node , Community, Article, Service , Donation , Event

from django.contrib.auth.models import User

class CommunityUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('firstName', 'lastName' , 'login' , 'password' , 'email' ,'birthday')

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('latitude', 'longitude' , 'community_name' , 'possessor' , 'state' , 'name', 'description')

class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'email' , 'original_node' , 'description' , 'facebook' , 'whatsapp' , 'twitter' , 'linkedin' , 'integrationProcess')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id', 'username', 'password']
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('title', 'publicator' , 'community' , 'content' , 'publication_date')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('name', 'node' , 'description')

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('title', 'author' , 'community' , 'description')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityUser
        fields = ('title', 'publicator' , 'community' , 'description' , 'lieu' , 'programmed_to' , 'publication_date')

