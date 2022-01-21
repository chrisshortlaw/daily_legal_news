from django.contrib import admin
from .models import Author, Article, Comment, Tag
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    list_filter = ('date',)
    search_fields = ('title', 'date', 'body')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'article', 'date', 'approved')
    list_filter = ('approved', 'date')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
