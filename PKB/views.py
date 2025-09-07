from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Shreyas Iyer is the Captain of PKB!')
def ViceCaptain(request):
    return HttpResponse('Marcus Stonnis is the Vice-Captain of PKB!')