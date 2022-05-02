from django.shortcuts import render
from django.views.generic import ListView, DetailView

from courses.models import Category, Course


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        return Course.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


def home(request):
    return render(request, 'base.html')