from django.urls import path
from MBA.views import *
app_name='MBA'
urlpatterns=[
    path('Course/',Course,name='Course'),
]