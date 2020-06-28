from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_photo')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%dd %H:%M:%S")
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

class Meta:
    ordering = ['-updated']

# Create your models here.
