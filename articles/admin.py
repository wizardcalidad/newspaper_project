from django.contrib import admin
#from django.contrib.admin import ModelAdmin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
