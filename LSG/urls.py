from django.urls import path
from LSG.views import Captain,ViceCaptain
app_name='LSG'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]