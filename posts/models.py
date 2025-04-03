from django.db import models

class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, default="Unknown")  # ここに default を追加
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
