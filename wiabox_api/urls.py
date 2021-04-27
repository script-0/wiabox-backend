from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'communityUser', views.CommunityUserViewSet)
router.register(r'community', views.CommunityViewSet)
router.register(r'node', views.NodeViewSet)
router.register(r'article', views.ArticleViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'Donation', views.DonationViewSet)
router.register(r'Event', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('platforms/', views.list_platform, name = 'platform'),
    path('platform/get', views.get_platform, name = 'platform'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
