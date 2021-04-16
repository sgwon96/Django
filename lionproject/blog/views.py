from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.writer = request.POST['writer']
    blog.pub_date = timezone.datetime.now()
    blog.image = request.FILES['image']
    blog.save()
    return redirect('/blog/' + str(blog.id))

def edit(request, blog_id):
    edit_blog = Blog.objects.get(id = blog_id)
    return render(request, 'blog/edit.html',{'blog':edit_blog})

def update(request, blog_id):
    update_blog = Blog.objects.get(id = blog_id)
    update_blog.title = request.POST['title']
    update_blog.body = request.POST['body']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = timezone.datetime.now()
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect('home')
