from rest_framework import serializers
from blog_n_events.models import Post, Category, Event


class СategoryPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description', 'create_at',)


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'create_at', 'author', 'category')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'create_at', 'author')