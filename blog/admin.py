from django.contrib import admin
from blog.models import Blog
from blog.models import Tag
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
