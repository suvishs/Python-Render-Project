from django.http import HttpResponse
from django.shortcuts import render

def demo(request):
    return render(request,'indux.html')
