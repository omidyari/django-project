from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import post
from datetime import date

# Create your views here.
def blog_home(request,**kwargs):
    stat_date = date(2020, 1, 1)
    end_date = date.today()
    posts = post.objects.filter(creted_date__range=(stat_date, end_date))
    if kwargs.get('cat') != None:
        posts = posts.filter(category__name=kwargs['cat'])
    if kwargs.get('user_n') != None:
        posts = posts.filter(escriber__username=kwargs['user_n'])
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

def blog_search(request):
    posts = post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(text__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)