from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(CommunityUser)
admin.site.register(Node)
admin.site.register(Community)
admin.site.register(Article)
admin.site.register(Service)
admin.site.register(Donation)
admin.site.register(Event)