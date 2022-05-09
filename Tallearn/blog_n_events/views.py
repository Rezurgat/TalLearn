from django.views.generic import ListView, DetailView, CreateView

from blog_n_events.models import Post, Event, Comment


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


