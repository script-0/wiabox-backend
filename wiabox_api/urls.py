from django.urls import include, path
from . import views

urlpatterns = [
    path('node/list', views.list_nodes),
    path('community/list', views.list_communities),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
