from django.views.generic import ListView, DetailView, CreateView

from blog_n_events.models import Post, Event, Comment, Category


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


