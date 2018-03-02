from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth import login, authenticate


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'registration/main.html')

def registration(request):
    if request.method=='POST':
        form = forms.UserForm(data=request.POST)
        if form.is_valid():

            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect('index')
    else:
        form = forms.UserForm()
    return render(request,'registration/registration.html',{'form':form})

def user_login(request):
    registered = False

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                registered = True
            else:
                return HttpResponse('ACCOUNT is NOT active')
        else:
            print('Someone tried to login but failed ')
            print('username:{} and password: {}'.format(username,password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request,'registration/login.html',{'registered':registered})

@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))