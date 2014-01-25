from django.contrib import admin
from asblog.models import Blog, Post

########################################################################
########################################################################
#
class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    #
    list_display = ['title', 'author']

    # fields to filter the change list with
    #
    list_filter = ['published', 'created', 'author']

    # fields to search in change list
    #
    search_fields = ['title', 'description', 'content']

    # enable the date drill down on change list
    #
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    #
    save_on_top = True

    # prepopulate the slug from the title - big timesaver!
    #
    prepopulated_fields = {"slug": ("title",)}

########################################################################
########################################################################
#
class PostInline(admin.TabularInline):
    model = Post
    extra = 1
    prepopulated_fields = {"slug": ("author", "title")}

########################################################################
########################################################################
#
class BlogAdmin(admin.ModelAdmin):
    # fields display on change list
    #
    list_display = ['title', 'description', 'owner', 'created']

    # fields to filter the change list with
    #
    list_filter = ['created', 'owner']

    # fields to search in change list
    #
    search_fields = ['title', 'description']

    # enable the date drill down on change list
    #
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    #
    save_on_top = True

    # prepopulate the slug from the title - big timesaver!
    #
    prepopulated_fields = {"slug": ("owner", "title")}

    # Posts are directly added from Blogs.
    #
    inlines = [PostInline]

admin.site.register(Blog, BlogAdmin)
# admin.site.register(Post, PostAdmin)

