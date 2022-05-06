from django.shortcuts import render
from django.views.generic import ListView, DetailView

from courses.models import Category, Course
from courses.forms import CommentForm


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
        return context


def home(request):
    return render(request, 'base.html')