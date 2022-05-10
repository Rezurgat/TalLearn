from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_at']


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_at', 'format']


