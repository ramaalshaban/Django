# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post #this is the moedel i created in the shell 
from django.views.generic import ListView

# the function here will handle the traffic from home 
# page of our blog   
# WHAT USER WILL SEE HRER

# the logic for how we want to handle when a user is in the cirtine page 
# NEXT
# Map our url pattern to this view
# in the url.py is where we map the url that we want to copprespond to each view function 
# --->
# def home(req):
#     return HttpResponse('<h1>Home</h1>')

# def about(req):
#     return HttpResponse('<h1>About</h1>')
#     set up the maping for this new path
from django.shortcuts import render

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    # here i am passing thewhole dictionary becouse ill go throu all the things using for loop
    # 
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # here we set new template so that we can use our existing template of the home page
    template_name = 'blog/home.html'
    # we still do not know what we want the variable to be named in out template
    # that we want to loop over like context

    # So we need variables to access to our templates to loop over
    # in the home function we called all post objects in the context
    # BUT by default THIS list view is going to call that variable: object list instead of :post
    # yani we want to pass object list for the list view not only objects
    # so we let the class know that we want that variable is called post
        # {% for post in posts %} #
    # to solve that we will change the name to posts here 
    context_object_name = 'posts'
    ordering= ['-date_posted']



def about(request):
    return render(request, 'blog/about.html', {'title': 'Some Titile '})


# ===========================
# class based views
#
# so far we have been using function based view
# url patterns are  directed to certin view that holds the function and the logics 
#  there is different class cased views: list views,detail views, create views, update views and delete views
# Django tries to predict these common bhavior and gves us a GENERIC

