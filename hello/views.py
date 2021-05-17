from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, This is Prashant's first webapp!")
