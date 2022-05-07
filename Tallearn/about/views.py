from django.views.generic import ListView

from about.models import About


class AboutListView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()

