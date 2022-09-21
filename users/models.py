
import queue
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# extending the already existed user model (Extending means adding new fielsd)


#django singles to run specific functions after certin actions.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# one on one with the user model 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #str method dender that mke us able tp specify how the data will be displaied 
    def __str__(self):
        return f'{self.user.username} Profile'

#if we want to show this model on the admin part i need to register this model on the admin filke