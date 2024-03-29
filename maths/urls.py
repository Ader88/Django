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
from .views import add, sub, mul, div, maths_list, add_result

urlpatterns = [
    path('add/<int:a>/<int:b>/', add, name='add'),
    path('sub/<int:a>/<int:b>/', sub, name='sub'),
    path('mul/<int:a>/<int:b>/', mul, name='mul'),
    path('div/<int:a>/<int:b>/', div, name='div'),
    path('maths/list/', maths_list, name='maths_list_url'),
    path('add_result/', add_result, name='add_result_url'),
]