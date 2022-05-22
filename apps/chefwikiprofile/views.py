from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CheferProfileForm

def cheferprofile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }

    return render(request, 'chefwikiprofile/chefwikiprofile.html', context)

@login_required
def follow_chefer(request,username):
    user = get_object_or_404(User, username=username)
    request.user.chefwikiprofile.follows.add(user.chefwikiprofile)

    return redirect('cheferprofile', username = username)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CheferProfileForm(request.POST, request.FILES,instance=request.user.chefwikiprofile)
    
        if form.is_valid():
            form.save()
            return redirect('cheferprofile', username=request.user.username)
    else:
        form = CheferProfileForm(instance=request.user.chefwikiprofile)
    
    context = {
        'user': request.user,
        'form': form
    }

    return render(request, 'chefwikiprofile/edit_profile.html', context)
