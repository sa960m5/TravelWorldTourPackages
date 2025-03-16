from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('packages', views.packages, name='packages'),
    path('vendors_packages', views.vendors_packages, name='vendors'),
    path('vendors_login', views.vendors_login, name='vendors_login'),
    path('vendors_home', views.vendors_home, name='vendors_home'),
    path('account/vendors_register', views.vendors_register, name='vendors_register'),
    path('approve_package/<int:package_id>/', views.approve_package, name='approve_package'),
    path('edit_package/<int:package_id>/', views.edit_package, name='edit_package'),
    path('delete_package/<int:package_id>/', views.delete_package, name='delete_package'),
]