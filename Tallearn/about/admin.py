from django.contrib import admin

from .models import About, Social


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'proficiency_level', 'create_at']
    list_display_links = ('firstname',)


admin.site.register(Social)
