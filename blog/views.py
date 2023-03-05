from django.shortcuts import render
from .models import Blog
# Create your views here.

def all_blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs/all_blogs.html',{'blogs':blogs})

def show_blog(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    return render(request,'blogs/detail.html',{'blog':blog})