"""
URL configuration for DjangoProject1 project.

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
from Sistema_Gestion import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farmacia/', views.farmacia, name='farmacia'),
    path('facturas/', views.facturas, name='facturas'),
    path('inventario/', views.inventario, name='inventario'),
    path('inicio/', views.inicio, name='inicio'),
    path('menu/', views.menu, name='menu'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),

    path('accounts/', include('django.contrib.auth.urls')),

 ]
