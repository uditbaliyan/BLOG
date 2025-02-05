"""
URL configuration for BLOG project.

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
from .views import *


urlpatterns = [
    # path('',front_page,name="front_page" ),
    path('home', Home.as_view(), name='Home'),
    path('post/<int:pk>/', Post_DetailView.as_view(), name='post_detail'),
    path('delete/<int:pk>/', Post_DeleteView.as_view(), name='post_delete'),
    path('update/<int:pk>/', Post_UpdateView.as_view(), name='post_update'),
    path('create/', Post_CreateView.as_view(), name='post_create'),
    path('', register, name='register'),

]
