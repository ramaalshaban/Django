from django.db.models.signals import post_save
# this is the signal that gets fired when a object is saved
# we will get a post save signal when a user is created

# the user here will be sender and also we need a reciver? 

from django.contrib.auth.models import User
# the reciver will get the signal and oreform some tasks
from django.dispatch import receiver
from .models import Profile

# we need to connect every new user with a profile ohoto


# So! WE have a sender in the line 16 
# when a user is saved then it will send a signal 
# the single will be recived by this reciver 
# reciver is actually a create profile function 
# the function has all those params that signal pasts to it 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # means if the usder is created
    if created:
        # crete a profile object with the instance of the user that we pass its enastance 
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()