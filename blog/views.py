# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post #this is the moedel i created in the shell 


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

def about(request):
    return render(request, 'blog/about.html', {'title': 'Some Titile '})


