from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    #if the user is login
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged In !")
            return redirect('home')
        else:
            messages.success(request, "There was an Error Loging In, Please Try Again.... !")
            return redirect('home')
    else:
        return render(request, 'home.html')
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Loged out...")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')
