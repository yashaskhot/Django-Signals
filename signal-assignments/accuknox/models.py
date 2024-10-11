from django.db import models

class YashasBlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class YashasComment(models.Model):
    post = models.ForeignKey(YashasBlogPost, on_delete=models.CASCADE)
    content = models.TextField()