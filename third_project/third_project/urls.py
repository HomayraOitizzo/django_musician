"""
URL configuration for third_project project.

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
from django.contrib import admin
from django.urls import path
from my_app import views

app_name = "my_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name="index"),
    path('home/', views.Home.as_view(), name="home"),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name="musician_details"),
    path('add_musician', views.AddMusician.as_view(), name="add_musician"),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name="musician_update"),
    path('delete_musician/<pk>/', views.DeleteMusician.as_view(), name="delete_musician"),

   
   

]

