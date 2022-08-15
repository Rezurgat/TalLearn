from rest_framework import generics
from courses.models import Category, Course, Comment
from api.courses_api.serializer_courses_api import (
    СategoryCourseListSerializer,
    CourseListSerializer,
    CourseDetailSerializer

)


class CategoryCourseListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = СategoryCourseListSerializer


class CourseListApiView(generics.ListAPIView):
    serializer_class = CourseListSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Course.objects.filter(category=category)


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
