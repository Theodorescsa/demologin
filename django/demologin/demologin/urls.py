"""demologin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from home import views as home
from profiles import views as profile_views
from django.urls import path,include
from profiles import views as profiles
from profiles.views import ViewUser



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home),  
    path('accounts/',include('django.contrib.auth.urls')),
   
    path('register/',profile_views.SiteRegisterView.as_view(),name='register'),    
   
    path('register/okey/',profile_views.SiteRegisterOkView.as_view(),name='dangkithanhcong'),    
    path('profile/',ViewUser.as_view(), name='user_view'),

    path('login/',profile_views.SiteLoginView.as_view(),name='login'),    
    path('profile/',profile_views.EditProfileView.as_view(),name='profile'),    
    path('home/', include('home.urls')),
]