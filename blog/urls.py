from django.urls import path
from blog.views import blog_home, blog_single, test, blog_search


app_name = 'blog'

urlpatterns = [
    path('blog_home', blog_home, name='blog_home'),
    path('<int:pid>', blog_single, name='blog_single'),
    path('category/<str:cat>', blog_home, name='category'),
    path('escriber/<str:user_n>', blog_home, name='escriber'),
    path('search/', blog_search, name='search'),
    path('test', test, name='test'),

]