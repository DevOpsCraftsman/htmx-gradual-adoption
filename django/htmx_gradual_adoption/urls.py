"""htmx_gradual_adoption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main import views


urlpatterns = [
    path('',                 views.LanguageList.as_view(),   name="list"),
    path('create/',          views.LanguageCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.LanguageUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', views.LanguageDelete.as_view(), name="delete"),
]
