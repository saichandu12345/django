from django.urls import path

from SRH.views import *

urlpatterns=[
    path('Captain/',Captain ,name='Captain'),
]