from django.contrib import admin
from .models import Post, Comment, Diary, DiaryComment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Diary)
admin.site.register(DiaryComment)