#!/usr/bin/env python
#
# File: $Id$
#
"""
ASBlog test cases.
"""

# system imports
#

# django imports
#
from django.test import TestCase
from django.contrib.auth.models import User

# app imports
#
from asblog.models import Blog, Post

# Create your tests here.

########################################################################
########################################################################
#
class BlogCreationTests(TestCase):

    ####################################################################
    #
    def setUp(self):
        """
        We need users for our tests..
        """
        self.user_1 = User.objects.create_user('Chevy Chase',
                                               'chevy@chase.com',
                                               'chevyspassword')
        return

    ####################################################################
    #
    def test_create(self):
        """
        Test the basics of a blog
        """
        blog = Blog(title = "Test", description = "No description",
                    owner = self.user_1 )
        blog.save()
