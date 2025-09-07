from django.urls import path
from SRH.views import Captain,ViceCaptain
app_name='SRH'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]