from django.urls import path
from Napp.views import about ,index, contact, elements


app_name = 'Napp'

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('elements', elements, name='elements'),
]