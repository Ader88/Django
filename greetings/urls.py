"""
URL configuration for dingo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'greetings'

urlpatterns = [
    path('', views.greet, name='greet'),
    path('name/<str:name>/', views.greet_name, name='greet_name'),
    path('welcome/', views.welcome, name="welcome_url"),
    path('about/', views.about, name="about_url"),
    path('contact/', views.contact, name="contact_url"),
]