from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Chips(request):
    return HttpResponse("<h2>Lays is always Best!</h2>")
def DairyMilk(request):
    return HttpResponse("<h1>Always Worst!!</h1>")