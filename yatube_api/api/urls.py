from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='Post')
router_v1.register('groups', GroupViewSet, basename='Group')
router_v1.register('follow', FollowViewSet, basename='Follow')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)

api_v1_urls = [
    path('', include(router_v1.urls)),
]

api_v1_urls += [
    path('', include('djoser.urls.jwt'))
]

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]
