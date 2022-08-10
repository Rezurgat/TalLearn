from rest_framework import generics
from about.models import About, Contact, Feedback
from api.about_api.serializer_about_api import AboutSerializer, ContactSerializer


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class ContactApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


