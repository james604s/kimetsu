from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from myauth.myauth import login_form
class MyLoginView(View):
    template_name = 'myauth/login.html'
    def get(self, request):
        return render(request, self.template_name, {'form':login_form})
    def post(self, request):
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse("login success")
            # return render(request, self.template_name, {'message':'Login Successful'})
        return HttpResponse("login failed")
        # return render(request, self.template_name, {'message':'Login Failed'})