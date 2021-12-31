from django.urls import path
from Napp.views import test ,index

urlpatterns = [
    path('test', test ),
    path('', index)
]
