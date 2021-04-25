from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'node', views.NodeViewSet)
router.register(r'community', views.CommunityViewSet)
router.register(r'platform', views.PlatformViewSet,basename='platform')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
