from django.shortcuts import  render,redirect
from . import forms
from . import models


def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()

                form.save_m2m()
                return redirect('dashboard')

        else:
            form = forms.PostForm()
        return render(request,'create_post.html',{'form': form})
    return redirect('signin')


def post_detail(request, id):
    post = models.Post.objects.get(pk=id)
    return render(request,'post_detailes.html',{'post':post})


def edit_post(request, id ):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == "POST":
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        form = post_form
        return render(request,'create_post.html',{'form':form})
    
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('dashboard')
    
    