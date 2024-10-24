"""
URL configuration for project4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app4.views import show_file,show_form,save_student,view_all,delete,delete_std
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show_file),
    path('show_form',show_form),
    path('save',save_student),
    path('view_all',view_all),
    path('delete',delete),
    path('delete_std',delete_std),
]
