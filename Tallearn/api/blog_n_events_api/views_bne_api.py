from rest_framework import generics
from blog_n_events.models import Post, Category, Event
from api.blog_n_events_api.serializer_bne_api import (
    PostListSerializer,
    PostDetailSerializer,
    СategoryPostListSerializer,
    EventListSerializer,
)

class CategoryPostListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = СategoryPostListSerializer

class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailApiView(generics.ListAPIView):
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category=category)

class EventListApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


