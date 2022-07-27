from rest_framework import generics
from blog_n_events.models import Post
from api.blog_n_events_api.serializer_bne_api import BlogPostSerializer

class BlogPostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer


