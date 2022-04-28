from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Category


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.all()

def home(request):
    return render(request, 'home.html')