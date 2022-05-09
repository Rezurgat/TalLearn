from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView

from about.models import About, Contact, Feedback
from about.forms import FeedbackForm


class AboutListView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()


class ContactView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        form = FeedbackForm()
        return render(request, 'about/contact.html', {"contacts": contacts, "form": form})


class CreateFeedback(SuccessMessageMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'about/contact.html'
    success_message = "Message was created successfully"

    def get_success_url(self):
        return self.request.path


