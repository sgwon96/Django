from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):
    form = BlogForm()
    return render(request, 'blog/new.html', {'form' : form})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.pub_date = timezone.now()
        blog.save()
        return redirect('blog:detail',blog.id)
    return redirect('blog:home')

def edit(request, blog_id):
    edit_blog = Blog.objects.get(id = blog_id)
    form = BlogForm(initial={
        'title' : edit_blog.title,
        'writer': edit_blog.writer,
        'image' : edit_blog.image,
        'body'  : edit_blog.body 
         })
    return render(request, 'blog/edit.html',{'form':form, 'blog_id':blog_id})

def update(request, blog_id):
    instance = Blog.objects.get(id=blog_id)
    form = BlogForm(request.POST,request.FILES, instance=instance)
    if form.is_valid():
        update_blog = form.save(commit=False)
        update_blog.pub_date = timezone.datetime.now()
        update_blog.save()
        return redirect('blog:detail',update_blog.id)
    return redirect('blog:home')

def delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return redirect('blog:home')
