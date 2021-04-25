from rest_framework import serializers

from .models import Node , Community , Platform

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('latitude', 'longitude' , 'community_name' , 'state' , 'name', 'description')


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'email' , 'original_node' , 'description')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ('name', 'key' , 'description')
