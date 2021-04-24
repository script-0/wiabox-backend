from django.db import models
from datetime import date
from django.utils import timezone

NODE_STATES = (
		('T' , 'Testing'),
		('R' , 'Running'),
		('W' , 'Working'),
	      )

NO_COMMUNITY = 0

# Node model.
class Node(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	community_name = models.CharField(max_length = 50)
	state = models.CharField(choices = NODE_STATES , max_length=1)
	name = models.CharField(max_length = 50)
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)	
	def __str__(self):
		return 'Node [ name = '+self.name+' ;'+' latitude = '+ self.latitude + ' ;' + ' longitude = '+ self.longitude + ' ;' + ' community = '+ self.community_name + ' ;'   + ' state = '+ self.state + ' ]'


# Community Model
class Community(models.Model):
	name =  models.CharField(max_length = 50, unique=True)
	email = models.EmailField()
	original_node = models.ForeignKey(Node, on_delete = models.SET(0))
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return 'Community [ name = '+ self.name + ' ; original_node = ' + self.original_node + ' ; description = ' + self.description + ' ] ' 
