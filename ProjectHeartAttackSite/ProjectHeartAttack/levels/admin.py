from django.contrib import admin

from .models import *


class LevelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_level', 'diffculty', 'author_level', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'name_level')
    search_fields = ('id', 'name_level', 'diffculty', 'autthor_level')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'context', 'timestamp', 'heart_comments')
    list_display_links = ('id', 'context')
    search_fields = ('id', 'context', 'timestamp')

# Register your models here.
admin.site.register(Levels, LevelsAdmin)
admin.site.register(Comment, CommentsAdmin)