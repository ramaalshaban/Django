
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
# here i am using the built in sytem for users 


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Create your models here.

    def __sre__(self):
        return self.title
        # search about this.
        #  get_absolute_url() a function that returns URL of a model object
        # by this method django know how to find specific location to specific post

        # the diff between redirect and reverse 







# the detqails that is printed out to be more discriptive

# .modelname_set
# special qurey set to user model
# something realted to user model
# here we are trying to get thePOSETS that the USER had created
# >>> user.post_set.create(title='blog3',content='third')
