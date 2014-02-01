# Django imports
#
from django.shortcuts import render

# 3rd party imports
#
from rest_framework import viewsets
from rest_framework import permissions

# ASBlog imports
#
from models import Blog, Post
from serializers import BlogSerializer, PostSerializer
from permissions import IsOwnerOrReadOnly


########################################################################
########################################################################
#
class BlogViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # XXX From our snippets REST tutorial.. left in here as a model for
    #     something we might want to do.
    #
    # @link(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    ####################################################################
    #
    def pre_save(self, obj):
        """
        Automatically set the owner of a blog when it is created.
        """
        obj.owner = self.request.user


########################################################################
########################################################################
#
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # XXX not linked to a blog?
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    ####################################################################
    #
    def pre_save(self, obj):
        """
        Automatically set the owner of a blog when it is created.
        """
        obj.author = self.request.user
