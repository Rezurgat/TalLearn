from rest_framework import serializers
from about.models import About, Contact, Feedback


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('firstname', 'lastname', 'proficiency_level', 'bio', 'link_telegram', 'link_instagram', 'link_vk', 'create_at')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('firstname', 'phone', 'link_telegram', 'link_website')


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


