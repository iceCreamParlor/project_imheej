from django.contrib import admin
from .models import Post, Comment, Diary, DiaryComment,Task

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Diary)
admin.site.register(DiaryComment)
admin.site.register(Task)