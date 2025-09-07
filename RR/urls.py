from django.urls import path
from RR.views import Captain,ViceCaptain
app_name='RR'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]