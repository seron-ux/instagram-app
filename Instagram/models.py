from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField('images')
    imageName = models.CharField(max_length=30,blank=True)
    imageCaption = models.CharField(max_length=300)
    # profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    # likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    # comments = models.CharField(max_length=30,blank=True)

    def savePost(self):
        print(self)
        return self.save()

