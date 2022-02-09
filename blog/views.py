from django.shortcuts import render
from blog.models import post

# Create your views here.
def blog_home(request):
    posts = post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
    
def blog_single(request):
    return render(request,'blog/blog-single.html')

