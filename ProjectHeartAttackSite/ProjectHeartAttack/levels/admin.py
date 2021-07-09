from django.contrib import admin

from .models import Levels


class LevelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_level', 'diffculty', 'autthor_level', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'name_level')
    search_fields = ('id', 'name_level', 'diffculty', 'autthor_level')

# Register your models here.
admin.site.register(Levels, LevelsAdmin)