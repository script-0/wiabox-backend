from django.contrib import admin

# Register your models here.
from .models import Node , Community , Platform
admin.site.register(Node)
admin.site.register(Community)
admin.site.register(Platform)
