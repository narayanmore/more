from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
@csrf_protect


def intro(request):
  s="hi am "
  return HttpResponse(s)


def intro2(request):
    res=render(request,'naru3app/naru3app.html') 
    return res