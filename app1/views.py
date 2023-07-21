from django.shortcuts import render
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h1>Hai How are you</h1>')
def second(request):
    return HttpResponse('<h1>hello</h1>')
