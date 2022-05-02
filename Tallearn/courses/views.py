from django.shortcuts import render
from django.views.generic import ListView, DetailView

from courses.models import Category


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

def home(request):
    return render(request, 'base.html')