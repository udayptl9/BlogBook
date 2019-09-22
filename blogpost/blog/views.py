from django.shortcuts import render, redirect, reverse
from .models import Posts
from .forms import Create
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Posts.objects.all().order_by('-id')
    context = {
        'title': 'Posts',
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def postView(request, postId):
    post = Posts.objects.get(id = postId)
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context)

@login_required
def postCreate(request):
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            newPost = Posts(title=request.POST['title'], content=request.POST['content'], auther=request.user)
            newPost.save()
            return redirect('blog-home')
    else:
            form = Create()
    context = { 'form': form }
    return render(request, 'blog/create.html', context)

@login_required
def postUpdate(request, pk):
    post = Posts.objects.get(id=pk)
    if post.auther == request.user:
        if request.method == "POST":
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('blog-home')
    else:
        return redirect('blog-home')
    context = {
        'post': post
    }
    return render(request, 'blog/update.html', context)

@login_required
def postDelete(request, pk):
    post = Posts.objects.get(id=pk)
    if post.auther == request.user:
        if request.method == "POST":
            post.delete()
            return redirect('blog-home')
    else:
        return redirect('blog-home')
    context = {
        'post': post
    }
    return render(request, 'blog/delete.html', context)
