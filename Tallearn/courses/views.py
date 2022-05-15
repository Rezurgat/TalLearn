from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from courses.models import Category, Course, Comment
from courses.forms import CommentForm

from about.models import About

from blog_n_events.models import Event, Post




class HomeView(ListView):
    model = Category
    template_name = 'courses/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_list'] = About.objects.all()
        context['event_list'] = Event.objects.all()
        context['blog_category_list'] = Post.objects.all()

        return context


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        return Course.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    slug_url_kwarg = 'course_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['course_list'] = Course.objects.all()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.course_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.course.get_absolute_url()


