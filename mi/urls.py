from mi.views import *

from django.urls import path

app_name='everything'

urlpatterns=[
    path('rahul/',rahul,name='rahul'),
    path('men/',men,name='men'),
]