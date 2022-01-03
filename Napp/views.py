from django.shortcuts import render

from django.http import HttpResponse, request
def contact(request):
    return render(request, 'main site/contact.html')
def index(request):
    return render(request, 'main site/index.html')
def about(request):
    return render(request, 'main site/about.html')
def elements(request):
    return render(request, 'main site/elements.html')