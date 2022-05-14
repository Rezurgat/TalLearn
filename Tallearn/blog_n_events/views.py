from django.http import HttpResponseRedirect
from django.shortcuts import redirect
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

    def get_ref(request):
        redirect_to = redirect('blog_n_events:post_list')
        return redirect_to


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    slug_url_kwarg = 'event_slug'



