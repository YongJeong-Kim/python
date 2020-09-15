from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from myapp.views import UserViewSet, UserDetailViewSet, PostViewSet

# user_list = UserViewSet.as_view({
#     'post': 'create',
#     'get': 'list',
# })

# post_list = PostViewSet.as_view({
#     'post': 'create',
#     # 'get': 'retrieve',
#     'get': 'list',
# })

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'posts', views.PostViewSet)
#
# urlpatterns = [
#     path('', include(router.urls))
# ]

# urlpatterns = format_suffix_patterns([
#     path('users/', user_list, name='user_list'),
#     path('posts/', post_list, name='post_list'),
# ])

urlpatterns = format_suffix_patterns([
    path('users/', UserViewSet.as_view(), name='user_list'),
    path('users/<int:id>', UserDetailViewSet.as_view(),name='user_detail'),
    path('posts/', PostViewSet.as_view(), name='post_list'),
])

