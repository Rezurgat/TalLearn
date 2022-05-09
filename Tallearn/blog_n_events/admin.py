from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_at']


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'create_at', 'format']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'create_at']
