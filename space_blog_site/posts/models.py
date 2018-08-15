from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    comments_num = models.IntegerField()
    likes_num = models.IntegerField()
    content = models.TextField()
    post_date = models.DateField()

    def __str__:
        return self.title

class Drafts(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    content = models.TextField()

    def __str__:
        return self.title

class Comments(models.Model):
    author = models.CharField(max_length = 200)
    content = model.TextField()
    post_date = model.DateField()

    def __str__:
        return self.author
