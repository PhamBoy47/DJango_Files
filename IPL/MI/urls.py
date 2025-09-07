from django.urls import path
from MI.views import Captain,ViceCaptain
app_name='MI'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]