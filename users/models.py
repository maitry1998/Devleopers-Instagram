from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null = True)
    email = models.EmailField(max_length = 500, blank =True, null=True)
    short_intro = models.CharField(max_length=200, blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null = True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profile-pics/',default="profile-pics/user-default.png")
    social_github = models.CharField(max_length=200,blank=True,null = True)
    social_twitter = models.CharField(max_length=200,blank=True,null = True)
    social_linkedin = models.CharField(max_length=200,blank=True,null = True)   
    social_youtube = models.CharField(max_length=200,blank=True,null = True)
    social_website = models.CharField(max_length=200,blank=True,null = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    location = models.CharField(max_length=200,blank=True,null = True)
    def __str__(self):
        return (self.user.username)


class Skill(models.Model):
    owner= models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null = True)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return (self.name)
    

class Message(models.Model):
    sender = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True)
    # if we dont add the related name here, it will cause an errir when we do profile.message_set.all() becuase there are two here with foreign key to profile
    recipient = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True, related_name="messages")
    name= models.CharField(max_length=200,null=True,blank=True)
    email= models.EmailField(max_length=200,null=True,blank=True)
    subject= models.CharField(max_length=200,null=True,blank=True)
    body= models.TextField()
    is_read =models.BooleanField(default=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return (self.subject)
    
    class Meta:
        ordering = ['is_read','-created']


# sender
# The model class.
    
# instance
# The actual instance being saved.
    
# created
# A boolean; True if a new record was created.

