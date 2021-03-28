from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Image(models.Model):
    image = models.ImageField('images')
    imageName = models.CharField(max_length=30,blank=True)
    imageCaption = models.CharField(max_length=300)
    comments = models.CharField(max_length=30,blank=True)
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    # likes = models.ManyToManyField(User, related_name='likes', blank=True, )
   

    def savePost(self):
        print(self)
        return self.save()



class Comment(models.Model):
    comment = models.TextField()
    postt= models.ForeignKey(Image, on_delete=models.CASCADE)
    userr= models.ForeignKey(pk = id,blank = True, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_now_add=True, null=True)


    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()


class Profile(models.Model):
    profilephoto = models.ImageField()
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,blank=True,related_name='follow')

    def __str__(self):
        return self.user.username


    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    



