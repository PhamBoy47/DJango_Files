from django.urls import path
from M_TECH.views import *
app_name='M_TECH'
urlpatterns=[
    path('Course/',Course,name='Course'),
]