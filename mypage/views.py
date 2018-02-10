from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.contrib import admin
from .forms import PostForm, DiaryForm, CommentForm, DiaryCommentForm
from .models import Post, Diary, Task
from django.shortcuts import render, get_object_or_404

# Create your views here.

def add_comment_to_diary(request, pk):
    post = get_object_or_404(Diary, pk=pk)
    if request.method == "POST":
        form = DiaryCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('mypage.views.diary_detail', pk=post.pk)
    else:
        form = DiaryCommentForm()
    return render(request, 'mypage/add_comment_to_diary.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('mypage.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'mypage/add_comment_to_post.html', {'form': form})

def index(request):
    posts = Post.objects.all()
    form = PostForm()

    tasks = Task.objects.order_by('date').all()

    context = {
        'form' : form,
        'posts' : posts,
        'tasks' : tasks,
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            '''post.author = request.user'''
            post.save()
            return render(request, 'mypage/index.html')
    else:
      form = PostForm()
      

    return render(request, 'mypage/index.html', context)
    #return render(request, 'mypage/index.html')
    
def profile(request):
    return render(request, 'mypage/profile.html')
    
def diary(request):
    posts = Diary.objects.all()
    form = DiaryForm()

    context = {
        'form' : form,
        'posts' : posts,
    }
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'mypage/index.html')
    else:
      form = DiaryForm()
      

    return render(request, 'mypage/diary.html', context)
    
    
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
            '''post.author = request.user'''
            post.save()
            return render(request, 'mypage/index.html')
    else:
      form = PostForm()
      

    return render(request, 'mypage/board.html', context)
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mypage/post_detail.html', {'post': post})

def diary_detail(request, pk):
    post = get_object_or_404(Diary, pk=pk)
    return render(request, 'mypage/diary_detail.html', {'post': post})