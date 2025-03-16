from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('vendors_login', views.vendors_login, name='vendors_login'),
    path('vendors_register', views.vendors_register, name='vendors_register'),
    path('accounts/logout/', LogoutView.as_view(), name='vendor_logout'),
    path('accounts/vendors_packages/', views.vendors_packages, name='vendor_packages'),
    path('accounts/vendors_home', views.vendors_home, name='vendors_home'),
    path('packages', views.packages, name='packages'),
]