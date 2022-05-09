from django.contrib import admin

from .models import About, Feedback


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname']
    list_display_links = ('firstname',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email_or_phone', 'message']
    list_display_links = ('firstname',)



