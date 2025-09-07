from django.urls import path
from GT.views import Captain,ViceCaptain
app_name='GT'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]