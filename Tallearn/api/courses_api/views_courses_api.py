from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Category, Course, Comment
from api.courses_api.serializer_courses_api import (
    СategoryCourseListSerializer,
    CourseListSerializer,
    CourseDetailSerializer,
    CommentCreateSerializer,
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


class CommentCreateApiView(APIView):

    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)
