from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.contrib import admin
from .forms import PostForm
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'mypage/index.html')
    
def consumer(request):
    return render(request, 'mypage/consumer.html')
    
def merchants_area(request):
    return render(request, 'mypage/merchants_area.html')
    
def vendors_area(request):
    return render(request, 'mypage/vendors_area.html')
    
def board(request):
    posts = Post.objects.all()
    form = PostForm()

    context = {
        'form' : form,
        'posts' : posts,
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'mypage/index.html')
    else:
      form = PostForm()
      

    return render(request, 'mypage/board.html', context)