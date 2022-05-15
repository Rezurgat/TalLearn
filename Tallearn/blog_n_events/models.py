from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category_blog_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_at']


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_articles/')
    slug = models.SlugField(max_length=50, default='')
    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.title}  {self.author} - ({self.create_at})'

    class Meta:
        ordering = ['create_at']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.category.slug, 'post_slug': self.slug})


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateTimeField()
    author = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return f'{self.title}  {self.author} - ({self.create_at})'

    class Meta:
        ordering = ['-create_at']

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_slug': self.slug})

