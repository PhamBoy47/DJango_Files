from django.urls import path
from BSC.views import *
app_name='BSC'
urlpatterns=[
    path('Course/',Course,name='Course'),
]