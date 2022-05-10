from django.views.generic import ListView, DetailView

from blog_n_events.models import Post, Event, Category


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


