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

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user = instance.user
    if not created: # it will cause recurwsion if dont write this statement due to the if condition in create profile
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
    print("profile saved")

def deleteUser(sender,instance,**kwargs):
    try:
        print("INSTANCE : ",instance)
        user = instance.user
        user.delete()
        print("deleting user")
    except AttributeError:
        # instance.delete()
        # Handle the case where instance doesn't have a user attribute
        return


post_save.connect(createProfile,sender=User)


post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)



# sender
# The model class.
    
# instance
# The actual instance being saved.
    
# created
# A boolean; True if a new record was created.


    