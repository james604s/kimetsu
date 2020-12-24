from django.urls import path
from myauth.views import *

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
]