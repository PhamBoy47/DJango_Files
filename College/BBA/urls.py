from django.urls import path
from BBA.views import *
app_name='BBA'
urlpatterns=[
    path('Course/',Course,name='Course'),
]