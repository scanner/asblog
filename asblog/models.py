from django.conf import settings
from django.db import models

# Create your models here.

########################################################################
########################################################################
#
class Blog(models.Model):
    """
    One blog.. it has an owner, posts, meta-data and permissions
    """
    title = models.CharField(max_length = 2048)
    slug = models.SlugField(unique = True, max_length = 255)
    description = models.CharField(max_length = 2048)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['title']

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
    blog = models.ForeignKey(Blog, null = False)
    title = models.CharField(max_length = 2048)
    slug = models.SlugField(max_length = 255)
    content = models.TextField()
    published = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['-created']
        unique_together = (("blog","slug"),)
        index_together = (("blog","slug"),)

    ####################################################################
    #
    def __unicode__(self):
        return u'%s' % self.title

    ####################################################################
    #
    def get_absolute_url(self):
        return reverse('asblog.views.post', args=[self.slug])

