from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Rishab Pant is the Captain of LSG!')
def ViceCaptain(request):
    return HttpResponse('Nicholas Pooran is the Vice-Captain of LSG!')