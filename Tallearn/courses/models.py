from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Модель категории курсов"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='category_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_category_url(self):
        """Метод для получения корректного url категории"""
        return reverse('course_list', kwargs={'slug': self.category.slug})


class Course(models.Model):
    """Модель курсов"""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='course_articles/')
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='course', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_at']

    def get_absolute_url(self):
        """Метод для корректного отображения url курса"""
        return reverse('course_detail', kwargs={'slug': self.category.slug, 'course_slug': self.slug})

    def get_comments(self):
        """Метод получения комментария"""
        return self.comment.all()

    def get_category_name(self):
        """Метод для получения и отображения имени категории в course_detail"""
        return self.category.name

    def get_category_slug(self):
        """Метод для получения и отображения url категории в course_detail"""
        return self.category.slug


class Comment(models.Model):
    """Модель комментариев"""
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



