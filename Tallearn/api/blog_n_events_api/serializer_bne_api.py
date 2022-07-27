from rest_framework import serializers
from blog_n_events.models import Post

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'description', 'create_at', 'author', 'category')