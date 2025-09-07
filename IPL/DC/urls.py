from django.urls import path
from DC.views import Captain,ViceCaptain
app_name='DC'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]