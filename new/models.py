from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Profile(models.Model):
    profilephoto = CloudinaryField('profilesss')
    Bio = models.CharField(max_length=30)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,blank=True,related_name='follow')

    def __str__(self):
        return self.user.username


    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()    


    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Followwww(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    followers = models.CharField(max_length=30)        

class Image(models.Model):
    image = CloudinaryField('images')
    imageName = models.CharField(max_length=30,blank=True)
    imageCaption = models.CharField(max_length=300)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=30,blank=True)

    def savePost(self):
        print(self)
        return self.save()

    
    @property
    def get_all_comments(self):
        return self.comments.all()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()    


    def __str__(self):
        return self.imageName    

class Comment(models.Model):
    comment = models.TextField()
    postt= models.ForeignKey(Image, on_delete=models.CASCADE)
    userr= models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def save_comment(self):
        self.user

    def delete_comment(self):
        self.delete()

