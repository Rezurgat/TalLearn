from rest_framework import generics
from courses.models import Category, Course, Comment
from serializer_courses_api import (
    СategoryCourseListSerializer,

)


class CategoryCourseListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = СategoryCourseListSerializer