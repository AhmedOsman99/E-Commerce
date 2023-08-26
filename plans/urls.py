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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_plans),
    path('<int:id>/', views.get_plan),
    path('add/', views.add_plan),
    path('edit/<int:id>/', views.edit_plan),
    path('delete/<int:id>/', views.delete_plan),
    path('cplan/', views.get_custom_plan),
    path('cplan/add/', views.add_custom_plan),
    path('cplane/edit/<int:id>/', views.edit_custom_plan),
    path('cplan/delete/<int:id>/', views.delete_custom_plan),
]
