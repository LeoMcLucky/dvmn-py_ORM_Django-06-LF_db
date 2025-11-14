from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = [
        'likes'
    ]

    list_display = [
        'title',
        'author',
        'published_at'
    ]


class TagAdmin(admin.ModelAdmin):
    list_display = [
        'title'
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'text',
        'post',
        'published_at'
    ]

    raw_id_fields = [
        'author',
        'post'
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
