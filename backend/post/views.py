from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from .utils import create_post
from django.views.decorators.csrf import csrf_exempt

import os, shutil, re
from django.core.files import File 
from django.conf import settings 


from django.http import JsonResponse
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/post.html', {'posts': posts})


def posting(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # set author as the current user
            post.save()
            
            return redirect('post:post')
    else:
        form = PostForm()
    return render(request, 'post/service-details.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'post/post_detail.html', {'post': post})


@csrf_exempt
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.delete()
        return JsonResponse({'success': True})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post:post_detail', pk=post.id)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'post/post_edit.html', {'form': form})
