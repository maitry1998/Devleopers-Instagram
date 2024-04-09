# @receiver(post_save,sender=Profile)
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

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
        subject = "Welcome aboard!!"
        message = "Welcome to the team! Think of our platform as the Instagram for developers—a community specially crafted for individuals like you, where you can connect, interact, and share with like-minded peers. Our hope is that within this vibrant pool of developers, you'll discover not just colleagues, but your favorite devs to collaborate and grow with. Welcome aboard, and let the creative synergy begin!"
        
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False
            )
        print("Email sent")

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user = instance.user
    if not created: # it will cause recurwsion if dont write this statement due to the if condition in create profile
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
        
    print("profile saved")

@receiver(post_delete,sender=Profile)
def deleteUser(sender,instance,**kwargs):
    try:
        # print("INSTANCE : ",instance)
        # import pdb;pdb.set_trace()
        user = instance.user
        user.delete()
        print("deleting user")
    except AttributeError:
        # instance.delete()
        # Handle the case where instance doesn't have a user attribute
        return


post_save.connect(createProfile,sender=User)


post_save.connect(updateUser,sender=Profile)
# post_delete.connect(deleteUser,sender=Profile)



# sender
# The model class.
    
# instance
# The actual instance being saved.
    
# created
# A boolean; True if a new record was created.


    