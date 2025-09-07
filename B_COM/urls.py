from django.urls import path
from B_COM.views import *
app_name='B_COM'
urlpatterns=[
    path('Course/',Course,name='Course'),
]