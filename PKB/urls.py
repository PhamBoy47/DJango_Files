from django.urls import path
from PKB.views import Captain,ViceCaptain
app_name='PKB'
urlpatterns=[
    path('captain/',Captain,name='captain'),
    path('vicecaptain/',ViceCaptain,name='vicecaptain'),
]