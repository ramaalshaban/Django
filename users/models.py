
from email.mime import image
import queue
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# extending the already existed user model (Extending means adding new fielsd)


# django singles to run specific functions after certin actions.
class Profile(models.Model):
    # one on one with the user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # str method dender that mke us able tp specify how the data will be displaied
    def __str__(self):
        return f'{self.user.username} Profile'

# if we want to show this model on the admin part i need to register this model on the admin filke

# here we are trying to "override the save method ??"
    def save(self):
        # here im calling the class that is already exist in the parent class //somethong about run the method?..
        super().save()
        # here we open the image for the instance that we are saving
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # save it back to the same path
            img.save(self.image.path)


# does each method has its own built in methods like save?
