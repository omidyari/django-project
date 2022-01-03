from django.urls import path
from Napp.views import about ,index, contact, elements

urlpatterns = [
    path('', index),
    path('about', about ),
    path('contact', contact),
    path('elements', elements),
]