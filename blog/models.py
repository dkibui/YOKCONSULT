from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'


class ActiveBlogManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().filter(active=1)


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=255, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    active = models.BooleanField(default=False, help_text='Select to Publish. De-Select un-publish')

    objects = models.Manager()
    active_blog = ActiveBlogManager()

    class Meta:
        ordering = ['date_posted', 'author']
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
