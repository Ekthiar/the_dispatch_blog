from django.shortcuts import render
from posts.models  import Post

# Create your views here.
def home_page(request):
    post = Post.objects.all()
    return render(request,"base.html", {'posts':post})