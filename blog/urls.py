from django.urls import path
from blog.views import blog_home, blog_single


app_name = 'blog'

urlpatterns = [
    path('blog_home', blog_home, name='blog_home'),
    path('blog_single', blog_single, name='blog_single')

]