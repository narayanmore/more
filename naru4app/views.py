from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
@csrf_protect
# Create your views here.


def info(request):
    res=render(request,'naru4app/naru4app.html')
    return res
