from django.shortcuts import render,redirect
from .forms import SignUpForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = SignUpForm()    
    return render(request,'users/register.html',{'form': form})    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_view')


    
