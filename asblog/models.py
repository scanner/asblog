#!/usr/bin/env python
#
# File: $Id$
#
"""
The Django models for our asblog Django app
"""

# system imports
#

# Django imports
#
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

# 3rd party module imports
#


########################################################################
########################################################################
#
class Blog(models.Model):
    """
    One blog.. it has an owner, posts, meta-data and permissions
    """
    title = models.CharField(_('title'), max_length=2048)
    slug = models.SlugField(_('slug'), unique=True, db_index=True,
                            max_length=255)
    description = models.CharField(_('description'), max_length=2048)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)

    class Meta:
        ordering = ['title']
        get_latest_by = "created"

    ####################################################################
    #
    def __unicode__(self):
        return u'%s' % self.title

    ####################################################################
    #
    def get_absolute_url(self):
        return reverse('asblog.views.blog', args=[self.slug])


########################################################################
########################################################################
#
class Post(models.Model):
    """
    Blogs have posts...
    """
    blog = models.ForeignKey(Blog, null=False, related_name="posts")
    title = models.CharField(_('title'), max_length=2048)
    slug = models.SlugField(_('slug'), max_length=255)
    content = models.TextField(_('content'))
    published = models.BooleanField(_('published'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)

    class Meta:
        ordering = ['-created']
        order_with_respect_to = "blog"
        get_latest_by = "created"
        unique_together = (("blog", "slug"),)
        index_together = (("blog", "slug"),)

    ####################################################################
    #
    def __unicode__(self):
        return u'%s' % self.title

    ####################################################################
    #
    def get_absolute_url(self):
        return reverse('asblog.views.post', args=[self.slug])
