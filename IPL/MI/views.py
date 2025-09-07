from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Hardik Pandya is the Captain of MI!')
def ViceCaptain(request):
    return HttpResponse('Surya Kumar Yadav is the Vice-Captain of MI!')