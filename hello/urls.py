"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

admin.site.site_header = "Codethon admin"
admin.site.site_title = "Codethon Admin Portal"
admin.site.index_title = "Welcome to our admin portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('testcase',include('home.urls')),
    path('contact',include("home.urls")),
    path('links',include("home.urls")),
    path('home',include("home.urls")),
    path('cirrhosis',include("home.urls")),
    path('brain_tumor',include("home.urls")),
    path('heart_disease',include("home.urls")),
    path('cirr',include("home.urls")),
    path('btumor',include("home.urls")),    
    path('hdisease2',include("home.urls")),
]
