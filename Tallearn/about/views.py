from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from about.models import About, Contact, Feedback
from about.forms import FeedbackForm

from blog_n_events.models import Post


class AboutListView(ListView):
    model = About

    def get_queryset(self):
        return About.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Post.objects.order_by('-create_at')[0:3]
        context['contact'] = Contact.objects.all()
        return context


class ContactListView(ListView):
    model = Contact

    def get(self, request):
        contacts = Contact.objects.all()
        blog = Post.objects.order_by('-create_at')[0:3]
        form = FeedbackForm()
        return render(request, 'about/contact_list.html', {"contacts": contacts, "form": form, 'blog': blog})



class CreateFeedback(SuccessMessageMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'about/contact_list.html'
    success_message = "Message was created successfully"

    def get_success_url(self):
        return self.request.path


