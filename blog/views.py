from django.shortcuts import render, get_object_or_404
from blog.models import post
from datetime import date

# Create your views here.
def blog_home(request):
    stat_date = date(2020, 1, 1)
    end_date = date.today()
    posts = post.objects.filter(creted_date__range=(stat_date, end_date))
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
    
def blog_single(request, pid):
    Post = get_object_or_404(post, pk=pid)
    context = {'Post':Post}
    return render(request,'blog/blog-single.html', context)

