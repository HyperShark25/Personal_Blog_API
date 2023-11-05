from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ["title", "author", "publish_date"]



admin.site.register(Blog, BlogAdmin)
