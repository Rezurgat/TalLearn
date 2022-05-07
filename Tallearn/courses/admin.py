from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_at']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'create_at']
