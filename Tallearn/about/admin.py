from django.contrib import admin

from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname',]
    list_display_links = ('firstname',)



