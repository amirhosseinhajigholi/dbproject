"""first_project URL Configuration

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
from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from app.views import MyView, MyView2 ,  Homee , SignUp , Costumerr , Paymentt , MyView4
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', MyView.as_view()),
    # path('accounts/login/', LoginView.as_view(template_name='login.html')),
    # path('accounts/profile/', login_required( TemplateView.as_view(template_name='profile.html')) ),
    # path('pattern/<str:code>', MyView2.as_view()),
    path('home/', Homee.as_view()) ,
    # path('accounts/signup/' ,  SignUp.as_view()),
    path('costumers/' ,  Costumerr.as_view()),
    path('payments/' ,  Paymentt.as_view()),
    path('cart/' ,  MyView4.as_view()),

    

]
