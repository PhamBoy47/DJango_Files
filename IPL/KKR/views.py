from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Ajinkaya Rahane is the Captain of KKR!')
def ViceCaptain(request):
    return HttpResponse('Venkatesh Iyer is the Vice-Captain of KKR!')