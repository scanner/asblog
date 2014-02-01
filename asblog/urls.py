# Django imports
#
from django.conf.urls import patterns, include, url

# 3rd party imports
#
from rest_framework_nested import routers

# asblog_dev imports
#
from views import BlogViewSet, PostViewSet


router = routers.SimpleRouter()
router.register(r'blogs', BlogViewSet)

blogs_router = routers.NestedSimpleRouter(router, r'blogs', lookup='blog')
blogs_router.register(r'posts', PostViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^', include(blogs_router.urls)),
)
