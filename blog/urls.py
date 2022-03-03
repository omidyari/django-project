from django.urls import path
from blog.views import blog_home, blog_single, test


app_name = 'blog'

urlpatterns = [
    path('blog_home', blog_home, name='blog_home'),
    path('<int:pid>', blog_single, name='blog_single'),
    path('test', test, name='test'),

]