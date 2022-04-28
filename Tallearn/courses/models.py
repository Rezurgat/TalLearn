from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='course_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='course',
        on_delete=models.CASCADE,
        null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=25, null=True, blank=True)
    comment_text = models.TextField(max_length=256)
    create_at = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(
        Course,
        related_name='comment',
        on_delete=models.CASCADE)

