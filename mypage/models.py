from __future__ import unicode_literals
from django.contrib import admin
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  "title : "+ self.title + "    "+ "date : " +  self.date.strftime("%Y-%m-%d %H:%M:%S")

class Diary(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


class DiaryComment(models.Model):
    post = models.ForeignKey(Diary)
    author = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.message

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    def __str__(self):
        return self.message
        
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_at']
    list_display_links = ['content']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'message', 'created_at']
    list_display_links = ['message']

class DiaryAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at']
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'content']
    list_display_links = ['message', 'date']