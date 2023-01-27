from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog
from datetime import date


def index(request):
    posts = Blog.objects.all().filter(active=1)
    return render(request, "blog/index.html", {'context': posts})


def blog_detail(request, slug):
    context = {}
    blog = Blog.objects.get(slug=slug)
    context['object'] = blog
    print(blog) 
    return render(request, "blog/a-blog.html", context)

