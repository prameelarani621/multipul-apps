from csk.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('abc/',abc,name='abc'),
]