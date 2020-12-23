from django.db import models
from django.contrib.auth.models import User

# users
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/')
    bio = models.CharField(max_length = 250)

    def __str__(self):
        return f'{self.User}'

# follow
class Following(models.Model):
    username = models.CharField(blank=True,max_length = 250)
    followed = models.CharField(blank=True,max_length = 250)

    def __str__(self):
        return f'{self.username}'
# posts
class Posts(models.Model):
    pic = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(blank=True,max_length = 250)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.profile.user.username}' 
        
# comments
class Comments(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 250)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'        