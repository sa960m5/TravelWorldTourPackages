from django.shortcuts import redirect, render, get_object_or_404
from .models import Package
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import PackageForm
from django.contrib.admin.views.decorators import staff_member_required

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
        return render(request, 'login.html')

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

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def vendors(request):
    return render(request, 'vendors.html')

def vendors_packages(request):
    return render(request, 'vendors_packages.html')

def vendors_home(request):
    return render(request, 'vendors_home.html')

def add_packages(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.approved = False  # Set package approval to False by default
            package.save()
            messages.success(request, "Package submitted for approval.")
            return redirect('vendors_packages')
    else:
        form = PackageForm()
    return render(request, 'add_packages.html', {'form': form})

@staff_member_required
def pending_packages(request):
    pending_packages = Package.objects.filter(approved=False)
    return render(request, 'pending_packages.html', {'pending_packages': pending_packages})

def packages(request):
    approved_packages = Package.objects.filter(approved=True)
    return render(request, 'packages.html', {'packs': approved_packages})

def vendors_packages(request):
    approved_packages = Package.objects.filter(approved=True)
    return render(request, 'vendors_packages.html', {'packs': approved_packages})

def edit_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            form.save()
            messages.success(request, "Package updated successfully.")
            return redirect('vendors_packages')
    else:
        form = PackageForm(instance=package)
    
    return render(request, 'edit_packages.html', {'form': form, 'package': package})

def delete_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    package.delete()
    messages.success(request, "Package deleted successfully.")
    return redirect('vendors_packages')