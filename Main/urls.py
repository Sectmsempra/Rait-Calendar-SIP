"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('', views.CS, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('cs/', views.CS, name="cs"),
    path('it/', views.IT, name="it"),
    path('extc/', views.EXTC, name="extc"),
    path('instru/', views.INSTRU, name="instru"),
    path('kalaraag/', views.KALARAAG, name="kalaraag"),
    path('suc/', views.SUC, name="suc"),
    path('acm/', views.ACM, name="acm"),
    path('gdsc/', views.GDSC, name="gdsc"),
    # path('search', views.search, name="search"),
    # path('signup', views.handleSignUp, name="handleSignUp"),
    # path('register/', views.registerPage, name='register'),
    # path('login/', views.loginPage, name='login'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    
]



