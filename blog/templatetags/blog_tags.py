from django import template
from blog.models import post, category

register = template.Library()

@register.simple_tag
def hello():
    return 'Hello mother fucker'

@register.inclusion_tag('blog/latestpost.html')
def latest_p():
    posts = post.objects.filter(status=1).order_by('published_date')
    context = {'posts': posts}
    return context
@register.inclusion_tag('blog/post-cat.html')
def post_cat():
    posts = post.objects.filter(status=1)
    categorys = category.objects.all()
    dic_cat= {}
    for name in categorys:
        dic_cat[name] = posts.filter(category=name).count()
    return {'categories': dic_cat}
