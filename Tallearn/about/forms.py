from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['create_at']
        widgets = {
         'firstname': forms.TextInput(attrs={'placeholder': 'Your Firstname'}),
         'lastname': forms.TextInput(attrs={'placeholder': 'Your Lastname'}),
         'email_or_phone': forms.TextInput(attrs={'placeholder': 'Your Email(for foreign students)/Phone number '}),
         'message': forms.TextInput(attrs={'placeholder': 'Which subject do you prefer?'}),
        }