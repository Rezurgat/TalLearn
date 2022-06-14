from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Модель категорий постов"""
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
    """Модель постов"""
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
        """Слаг поста"""
        return reverse('post_detail', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_category_name(self):
        """Отображение имени конкретной категории"""
        return self.category.name

    def get_category_slug(self):
        """Отображение слага конкретной категории"""
        return self.post.slug

class Event(models.Model):
    """МОдель события"""
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
        """Возврат слага события """
        return reverse('event_detail', kwargs={'event_slug': self.slug})

