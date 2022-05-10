# Generated by Django 4.0.4 on 2022-05-10 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(upload_to='category_blog_articles/')),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
                ('format', models.CharField(max_length=50)),
                ('slug', models.SlugField(default='')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog_articles/')),
                ('slug', models.SlugField(default='')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog_n_events.category')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(max_length=256)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog_n_events.post')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
    ]
