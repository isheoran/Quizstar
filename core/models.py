from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
import uuid, datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    name = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='blank-profile-picture.png')
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user  = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'post_images')
    title = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    blog_text = models.TextField()

    def __str__(self):
        return self.user

class Question(models.Model):
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.question

class Puzzle(models.Model):
    title = models.TextField()
    question = models.TextField()
    ans = models.TextField()

    def __str__(self):
        return self.question
    