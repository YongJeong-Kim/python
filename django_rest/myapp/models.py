from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
