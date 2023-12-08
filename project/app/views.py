from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("your password and confirm password are not same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            redirect('login')
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username and passwords are not correct")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')