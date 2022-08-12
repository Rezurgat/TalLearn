from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from about.models import About, Contact, Feedback
from api.about_api.serializer_about_api import (
    AboutSerializer,
    ContactSerializer,
    FeedbackCreateSerializer,

)


class AboutApiView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    

class ContactApiView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class FeedbackCreateApiView(APIView):

    def post(self, request):
        feedback = FeedbackCreateSerializer(data=request.data)
        if feedback.is_valid():
            feedback.save()
        return Response(status=201)
