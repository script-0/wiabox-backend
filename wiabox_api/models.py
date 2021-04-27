from django.db import models
from datetime import date
from django.utils import timezone

NODE_STATES = (
		('T' , 'Testing'),
		('R' , 'Running'),
		('W' , 'Working'),
	      )

INTEGRATION_PROCESSES = (
	('T' , 'Testing'),
	('W' , 'Working'),
)

NO_COMMUNITY = 'NO COMMUNITY'

class CommunityUser(models.Model):
	firstName =  models.CharField(max_length = 50, unique=True)
	lastName =  models.CharField(max_length = 50, unique=True)
	login =  models.CharField(max_length = 10, unique=True)
	password = models.CharField(max_length = 256, unique=True)
	email = models.EmailField()
	birthday = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.firstName + self.lastName

class Node(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	community_name = models.CharField(max_length = 50 , default = NO_COMMUNITY)
	possessor = models.ForeignKey(CommunityUser, default=0, on_delete = models.SET(0))
	state = models.CharField(choices = NODE_STATES , max_length=1)
	name = models.CharField(max_length = 50)
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	'''
		def __str__(self):
			return 'Node [ name = '+self.name+' ;'+' latitude = '+ str(self.latitude) + ' ;' + ' longitude = '+ str(self.longitude) + ' ;' + ' community = '+ self.community_name + ' ;'   + ' state = '+ self.state + ' ]'
	'''

class Community(models.Model):
	name =  models.CharField(max_length = 50, unique=True)
	email = models.EmailField()
	original_node = models.ForeignKey(Node, on_delete = models.SET(0))
	description = models.TextField(null=True)
	facebook = models.TextField(null=True)
	whatsapp = models.TextField(null=True)
	twitter = models.TextField(null=True)
	linkedin = models.TextField(null=True)
	integrationProcess = models.CharField(choices = INTEGRATION_PROCESSES , max_length=1)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	'''
		def __str__(self):
			return 'Community [ name = '+ self.name + ' ; original_node = ' + str(self.original_node) + ' ; description = ' + self.description + ' ] '
	'''

class Article(models.Model):
	title =  models.CharField(max_length = 50, unique=True)
	publicator = models.ForeignKey(CommunityUser, on_delete = models.SET(0))
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	content = models.TextField(null=True)
	publication_date = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)

class Service(models.Model):
	name =  models.CharField(max_length = 50, unique=True)
	node = models.ForeignKey(Node, on_delete = models.SET(0))
	description = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)

class Donation(models.Model):
	title =  models.CharField(max_length = 50, unique=True)
	author =  models.CharField(max_length = 50, unique=True)
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	description = models.TextField(null=True)
	create_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)

class Event(models.Model):
	title =  models.CharField(max_length = 50, unique=True)
	publicator = models.ForeignKey(CommunityUser, on_delete = models.SET(0))
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	description = models.TextField(null=True)
	lieu = models.TextField(null=True)
	programmed_to = models.DateTimeField(auto_now_add=True)
	publication_date = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)