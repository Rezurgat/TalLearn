from django.views.generic import ListView

from about.models import About, Contact


class AboutListView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()


class ContactListView(ListView):
    model = Contact

    def get_queryset(self):
        return Contact.objects.all()

