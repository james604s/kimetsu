from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from myauth.myauth import login_form
class MyLoginView(View):
    template_name = 'myauth/login.html'
    def post(self, request):
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse("Login Successful")
        return HttpResponse("Login Failed")