from django.shortcuts import render
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>what are you doing</h1>')
def second(request):
    return HttpResponse('<h1>Bye...</h1>')
