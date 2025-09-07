from django.urls import path
from RCB.views import Captain,ViceCaptain
app_name='RCB'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]