from django.shortcuts import render, redirect
from . import forms
from posts.models import Post



def profile(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = forms.ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                form = forms.ProfileForm()
        else:
            form = forms.ProfileForm()
        return render(request, 'profilePage.html', {'form': form})
    else:
        return redirect('signin')
    
def edit_profile1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.EditProfileForm1(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = forms.EditProfileForm1(instance = request.user)
        return render(request, 'editProfilePage.html', {'form': form})
    else:
        return redirect('signin')
    
def edit_profile2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.ProfileForm(request.POST, instance = request.user)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('profile')
        else:
            form = forms.ProfileForm(instance=request.user)
        return render(request, 'editProfilePage.html', {'form': form})
    else:
        return redirect('signin')
    

 
def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.filter(author= request.user)
        return render(request, 'dashboardPage.html', {'posts': post})
    else:
        return redirect('home')
    
