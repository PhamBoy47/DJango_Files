from django.urls import path
from KKR.views import Captain,ViceCaptain
app_name='KKR'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]