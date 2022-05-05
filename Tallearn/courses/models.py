from django.db import models
from django.urls import reverse
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
    head_slug = models.CharField(max_length=50, default='', null=True, blank=True)
    head_title = models.CharField(max_length=100, default='', null=True, blank=True)
    head_description = models.TextField(default='', null=True, blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='course_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='course', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.category.slug, 'course_slug': self.slug})


class Comment(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    comment = models.TextField(max_length=256)
    create_at = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname}  {self.lastname} - ({self.email})'

    class Meta:
        ordering = ['create_at']

