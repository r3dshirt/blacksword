from blog.models import Blog
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'pub_date']}),
        (None, {'fields':['body']}),
    ]

admin.site.register(Blog, BlogAdmin)