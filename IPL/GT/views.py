from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Shubman Gill is the Captain of GT!')
def ViceCaptain(request):
    return HttpResponse('Rashid Khan is the Vice-Captain of GT!')