from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Course(request):
    return HttpResponse('This is BBA Course')