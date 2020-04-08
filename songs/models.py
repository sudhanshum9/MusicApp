from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Rating(models.Model):
    rating = models.IntegerField()


class Song(models.Model):
    Name = models.CharField(max_length=100)
    Date_of_Release = models.CharField(max_length=15)
    #date_posted = models.DateTimeField(default=timezone.now)
    artist = models.CharField(max_length=100)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user= models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    def __str__(self):
        return self.Name
    def save(self):
        super().save()
"""
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)"""

class Artist(models.Model):
    artist = models.TextField(max_length=30,default="null")
    DOB = models.TextField(max_length=15)
    Bio = models.TextField(max_length=150)

    def __str__(self):
        return self.artist

    def save(self):
        super().save()
