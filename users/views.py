
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("heeeeereeeeeeeeeeeee", username)
            messages.success(
                request, f'Sayin {username} Your account has been created! you are now able to log in.')
            return redirect('login')
        # create a form that has req.post data
        # when it gets a post req it it will
        # instantiate a user creation form
        # with the post data
    else:
        form = UserRegisterForm()
        # here it instantioate an empty form
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Sayin {username} Your account has been updated!')
            return redirect('profile')
# here i used redirect not render becuse of something called the
#  post get redirect pattern 
# because when i redirect i sent a get request that will not be the reason 
# to create new post request and there for new form

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
# Remember when we submit forms its going to do a post request back
# to the same routes with the data from the form

# Populate regular forms??
# models forms always expecting the work on specific objects









