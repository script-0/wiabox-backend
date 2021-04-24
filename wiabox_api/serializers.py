from rest_framework import serializers

from .models import Node , Community

class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = ('latitude', 'longitude' , 'community_name' , 'state' , 'name', 'description')


class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'email' , 'original_node' , 'description')

