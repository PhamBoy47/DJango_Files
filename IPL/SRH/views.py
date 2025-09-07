from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Pat Cummins is the Captain of SRH!')
def ViceCaptain(request):
    return HttpResponse('Henrich Klassen is the Vice-Captain of SRH!')