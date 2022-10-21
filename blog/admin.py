from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tags","date",)
    list_display = ("title","author","date",)
    prepopulated_fields= {"slug":("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name","post","text",)

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
