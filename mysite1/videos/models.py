from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('web开发', 'web开发'),
        ('其他', '其他'),
    ]
    
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='其他')  # 添加分类字段
    
    def __str__(self):
        return self.title

class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)