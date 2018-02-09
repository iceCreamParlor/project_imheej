from django import forms
from .models import Post, Comment, Diary

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message',)
        
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content']