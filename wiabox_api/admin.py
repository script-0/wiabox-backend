from django.contrib import admin

# Register your models here.
from .models import Node , Community
admin.site.register(Node)
admin.site.register(Community)
