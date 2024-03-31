from django.contrib import admin

from virtualtour import models


@admin.register(models.Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title', 'slug']

@admin.register(models.Video)
class TourVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour', 'video_file', 'ordering', 'created_at', 'updated_at']
