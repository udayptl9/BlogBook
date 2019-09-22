from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistraionForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# user registraion
def register(request):
    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'account created for {username}')
            return redirect('login')
    else:
        form = UserRegistraionForm()
    return render(request, 'users/register.html', {'form': form, 'title': f'User - Create'})

# profile view and update
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated Successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': f'Profile - {request.user.username}'
    }
    return render(request, 'users/profile.html', context)

def UserDetailView(request, UserName):
    user = User.objects.get(username = UserName)
    context = {
        'user': user
    }
    return render(request, 'users/user_detail.html', context)
