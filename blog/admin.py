from django.contrib import admin

# Register your models here.

# here we aadd our models so it 
#  show up in the admin pannek 
from .models import Post

admin.site.register(Post)
# NICE GUI