from django.urls import path
from MSC.views import *
app_name='MSC'
urlpatterns=[
    path('Course/',Course,name='Course'),
]