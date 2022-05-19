from django.views.generic import ListView, DetailView

from blog_n_events.models import Post, Event, Category

from about.models import Contact


class CategoryListView(ListView):
    model = Category
    context_object_name = 'blog_category_list'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        return context


class EventListView(ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Post.objects.order_by('-create_at')[0:3]
        context['contact'] = Contact.objects.all()
        return context


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    slug_url_kwarg = 'event_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Post.objects.order_by('-create_at')[0:3]
        context['contact'] = Contact.objects.all()
        return context
