from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Captain(request):
    return HttpResponse('Axar Patel is the Captain of DC!')
def ViceCaptain(request):
    return HttpResponse('Fab DuPlessis is the Vice-Captain of DC!')