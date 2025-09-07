from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Sanju Samson is the Captain of RR!')
def ViceCaptain(request):
    return HttpResponse('Riyan Paraag is the Vice-Captain of RR!')