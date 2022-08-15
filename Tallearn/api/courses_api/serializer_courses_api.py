from rest_framework import serializers
from courses.models import Category, Course, Comment


class СategoryCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'create_at',)


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'slug', 'description', 'create_at', 'category')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    comment = CommentCreateSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'


