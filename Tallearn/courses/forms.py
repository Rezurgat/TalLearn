from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'course']
        widgets = {
         'firstname': forms.TextInput(attrs={'placeholder': 'Your Firstname'}),
         'lastname': forms.TextInput(attrs={'placeholder': 'Your Lastname'}),
         'email': forms.TextInput(attrs={'placeholder': 'Your Email'}),
         'comment': forms.Textarea(attrs={'cols': 87, 'rows': 10, 'placeholder': 'Your Message'}),
        }