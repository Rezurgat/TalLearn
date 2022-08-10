from rest_framework import generics
from blog_n_events.models import Post, Category, Event
from api.blog_n_events_api.serializer_bne_api import BlogPostSerializer, СategoryPostSerializer, EventSerializer

class CategoryPostApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = СategoryPostSerializer

class BlogPostApiView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(category=category)

class EventApiView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


