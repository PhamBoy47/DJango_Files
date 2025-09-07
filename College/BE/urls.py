from django.urls import path
from BE.views import *
app_name='BE'
urlpatterns=[
    path('Course/',Course,name='Course'),
]