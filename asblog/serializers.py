#!/usr/bin/env python
#
# File: $Id$
#
"""
Serializers.. modeled very much like django-forms but are a way to
reprent your models and such data collections so the REST framework can
serialize them for callers.
"""

# system imports
#

# Django imports
#
from django.conf import settings

# 3rd party imports
#
from rest_framework import serializers

# asblog imports
#
from asblog.models import Blog, Post


########################################################################
########################################################################
#
class BlogSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.RelatedField()
    owner_id = serializers.Field(source='owner.id')
    posts = serializers.HyperlinkedIdentityField(view_name='post-list')

    class Meta:
        model = Blog
        fields = ('url', 'title', 'description', 'created', 'updated',
                  'owner', 'owner_id', 'posts')


########################################################################
########################################################################
#
class PostSerializer(serializers.HyperlinkedModelSerializer):
    blog = serializers.HyperlinkedRelatedField(read_only=True,
                                               view_name='blog-detail')
    author = serializers.Field(source='author')

    class Meta:
        model = Post
        fields = ('title', 'content', 'published', 'created', 'updated',
                  'author')
