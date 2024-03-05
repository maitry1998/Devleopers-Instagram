# @receiver(post_save,sender=Profile)
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User

def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name= user.first_name,
        )
    print("profile saved")

def deleteUser(sender,instance,created,**kwargs):
    user = instance.user
    user.delete()
    print("deleting user")

post_save.connect(createProfile,sender=User)
post_delete.connect(deleteUser,sender=Profile)
    