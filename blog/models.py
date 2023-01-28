from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=255, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    active = models.BooleanField(
        default=False, help_text="Select to Publish. De-Select un-publish"
    )

    class Meta:
        ordering = ["date_posted", "author"]
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
