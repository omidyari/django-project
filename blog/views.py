from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import post
from datetime import date

# Create your views here.
def blog_home(request):
    stat_date = date(2020, 1, 1)
    end_date = date.today()
    posts = post.objects.filter(creted_date__range=(stat_date, end_date))
    #pagination
    #paginator = Paginator(posts, 3)
    #page = request.GET.get('page')
    #articles =  paginator.get_page(page)

    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
    
def blog_single(request, pid):
    Post = get_object_or_404(post, pk=pid)
    nextp = post.objects.filter(id__gt=Post.pk).order_by('pk').first()
    prep = post.objects.filter(id__lt=Post.pk).order_by('pk').last()
    context = {'Post':Post, 'nextp':nextp, 'prep':prep}
    return render(request,'blog/blog-single.html', context)

def test(request):
    return render(request,'test.html')
