from rcb.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('ram/',ram,name='ram'),
]