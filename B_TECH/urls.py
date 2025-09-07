from django.urls import path
from B_TECH.views import *
app_name='B_TECH'
urlpatterns=[
    path('Course/',Course,name='Course'),
]