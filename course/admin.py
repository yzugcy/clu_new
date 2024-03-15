from django.contrib import admin

from course import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'total_module', 'is_active', 'created_at', 'updated_at'
    ]
    search_fields = ['title']


@admin.register(models.CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'ordering', 'course', 'total_content', 'is_active',
        'created_at', 'updated_at'
    ]


@admin.register(models.CourseContent)
class CourseContentAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'course_module', 'is_active', 'created_at', 'updated_at'
    ]


@admin.register(models.CourseContentReadStatus)
class CourseContentReadStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_read', 'created_at', 'updated_at']
