from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                username =request.POST['username']
                password = request.POST['password']
                user = authenticate(request , username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        return render(request,'accounts/login.html')            
    else:
        return redirect('/')
@login_required      
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print("why")
        form =UserCreationForm()
    else:
        return redirect('/')
    return render(request,'accounts/signup.html')     



