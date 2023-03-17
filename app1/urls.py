from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('chennai/',chennai,name='chennai'),
    path('delhi/',delhi,name='delhi'),
]