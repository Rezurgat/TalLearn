from rest_framework import serializers
from courses.models import Category, Course, Comment

class СategoryCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'create_at',)