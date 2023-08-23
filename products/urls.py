"""
URL configuration for E_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_products),
    path('<int:id>/', views.get_product),
    path('add/', views.add_product),
    path('edit/<int:id>/', views.edit_product),
    path('delete/<int:id>/', views.delete_product),
    path('category/', views.list_categories),
    path('category/<int:id>/', views.get_category),
    path('category/add/', views.add_category),
    path('category/edit/<int:id>/', views.edit_category),
    path('category/delete/<int:id>/', views.delete_category),
]
