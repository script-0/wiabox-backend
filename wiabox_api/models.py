from django.db import models
from datetime import date
from django.utils import timezone
from django import forms

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
	firstName =  models.CharField(max_length = 256)
	lastName =  models.CharField(max_length = 256)
	login =  models.CharField(max_length = 256, unique=True)
	password = models.CharField(max_length = 256)
	email = models.EmailField()
	birthday = models.DateTimeField(auto_now_add=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.firstName + ' ' + self.lastName

class Node(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	community_name = models.CharField(max_length = 256 , default = NO_COMMUNITY)
	possessor = models.ForeignKey(CommunityUser, null=True, on_delete = models.SET(0))
	state = models.CharField(choices = NODE_STATES , max_length=256)
	name = models.CharField(max_length = 256)
	description = models.TextField(null=True , blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	'''
		def __str__(self):
			return 'Node [ name = '+self.name+' ;'+' latitude = '+ str(self.latitude) + ' ;' + ' longitude = '+ str(self.longitude) + ' ;' + ' community = '+ self.community_name + ' ;'   + ' state = '+ self.state + ' ]'
	'''

class Community(models.Model):
	name =  models.CharField(max_length = 256, unique=True) 
	email = models.EmailField()
	original_node = models.ForeignKey(Node, on_delete = models.SET(0))
	description = models.TextField(null=True , default = '', blank=True)
	facebook = models.TextField(null=True , default = '', blank=True)
	whatsapp = models.TextField(null=True , default = '', blank=True)
	twitter = models.TextField(null=True , default = '', blank=True)
	linkedin = models.TextField(null=True , default = '', blank=True)
	integrationProcess = models.CharField(choices = INTEGRATION_PROCESSES , max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	'''
		def __str__(self):
			return 'Community [ name = '+ self.name + ' ; original_node = ' + str(self.original_node) + ' ; description = ' + self.description + ' ] '
	'''

class Article(models.Model):
	title =  models.CharField(max_length = 256, unique=True)
	publicator = models.ForeignKey(CommunityUser, on_delete = models.SET(0))
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	content = models.TextField()
	publication_date = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class Service(models.Model):
	name =  models.CharField(max_length = 256, unique=True)
	node = models.ForeignKey(Node, on_delete = models.SET(0))
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

class Donation(models.Model):
	title =  models.CharField(max_length = 256, unique=True)
	author =  models.CharField(max_length = 256, unique=True)
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	description = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title

class Event(models.Model):
	title =  models.CharField(max_length = 256, unique=True)
	publicator = models.ForeignKey(CommunityUser, on_delete = models.SET(0))
	community = models.ForeignKey(Community, on_delete = models.SET(0))
	description = models.TextField()
	lieu = models.TextField(null=True)
	programmed_to = models.DateTimeField(auto_now_add=True)
	publication_date = models.DateTimeField(auto_now_add=True)
	last_updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title