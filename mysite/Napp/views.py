from django.shortcuts import render

from django.http import HttpResponse, request
def test(request):
    return HttpResponse('<h1>hi dear user</h1>')
def index(request):
    return render(request, 'index.html')