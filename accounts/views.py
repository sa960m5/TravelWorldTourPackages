from importlib.resources import Package
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
    
def vendors_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('vendors_packages')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('vendors_login')
    else:
        return render(request, 'vendors_login.html')
    
def vendors_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('vendors_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('vendors_register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "vendor created...")
                return redirect('vendors_login')
        else:
            messages.info(request, "password not matched...")
            return redirect('vendors_register')
        return redirect('/vendors')
    else:
        return render(request, 'vendors_register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def vendors_logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def packages(request):
    approved_packages = Package.objects.filter(approved=True)
    return render(request, 'packages.html',{'packs': approved_packages})

def vendors_packages(request):
    approved_packages = Package.objects.filter(approved=True)
    return render(request, 'vendors_packages.html', {'packs': approved_packages})

def vendors_home(request):
    return render(request, 'vendors_home.html')