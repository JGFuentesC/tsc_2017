from django.conf.urls import url, include
from .views import *

app_name = "login"

urlpatterns = [
    url(r'^', index, name='login')
]
