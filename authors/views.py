from django.shortcuts import  render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import logout, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm 


def registration(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, 'Registration complete!')
            return redirect('dashboard')
    else:
        form = forms.RegistrationForm()
    return render(request, 'RegistrationPage.html', {'form': form})


def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect("dashboard")
        else:
            form = AuthenticationForm()
        return render(request,'signinPage.html',{'form':form})
    else:
        return redirect("dashboard")


def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RetsetPasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                
                messages.success(request,"your password has been changed successfully")
                return redirect('profile')
        else:
            form = forms.RetsetPasswordForm(request.user)
        return render(request, 'passwordChagePage.html', {'form': form})
    else:
        return redirect('signin')
        

def signout(request):
    logout(request) 
    return redirect('signin')