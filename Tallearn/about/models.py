from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class About(models.Model):
    head_title = models.CharField(max_length=100, null=True, blank=True)
    head_description = RichTextField(null=True, blank=True)
    head_teachers = models.CharField(max_length=100, null=True, blank=True)
    teachers_description = RichTextField(null=True, blank=True)
    photo = models.FileField(upload_to='about/')
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    proficiency_level = RichTextField()
    bio = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname}  {self.lastname}'

    class Meta:
        ordering = ['create_at']


class Social(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField()
    about = models.ForeignKey(
        About,
        related_name='social',
        on_delete=models.CASCADE)

class Feedback(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    message = models.TextField(max_length=256)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.firstname}  {self.lastname} - ({self.email})'

    class Meta:
        ordering = ['create_at']



