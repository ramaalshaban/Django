
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

# Create your views here.

def register(request):
 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("heeeeereeeeeeeeeeeee", username)
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
        # create a form that has req.post data
        # when it gets a post req it it will
        # instantiate a user creation form
        # with the post data
    else:
        form = UserRegisterForm()
        # here it instantioate an empty form 
    return render(request, 'users/register.html',{'form':form})
    