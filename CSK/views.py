from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('MSD is the Captain of CSK!')
def ViceCaptain(request):
    return HttpResponse('Suresh Raina is the Vice-Captain of CSK!')