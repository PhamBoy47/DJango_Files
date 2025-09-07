from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Biriyani(request):
    return HttpResponse("<h1>Panner Biriyani</h1>")
def Kabab(request):
    return HttpResponse("Kabab is average!")