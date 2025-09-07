from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Rajat Pattidar is the Captain of RCB!')
def ViceCaptain(request):
    return HttpResponse('Jitesh Sharma is the Vice-Captain of RCB!')