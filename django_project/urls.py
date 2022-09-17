"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views

# which routs should go to our blog urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    # this is another way to build a url pattern
    path('', include('blog.urls')),

    # send an empty string to blog urls
# here when it passes this to the urls of the app
# it for further process it is going to chop pff
# the alredy mached part and only send the remaining string

]

# here we set up the mappig from certain urls to where we sent the user so 

# this will tell our whole website which urls should send us to our blog a[[??]]