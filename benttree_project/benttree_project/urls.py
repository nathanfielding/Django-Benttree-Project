"""benttree_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from benttree_api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),

    #tenant endpoints
    path("tenants/", TenantList.as_view()),
    path("tenants/by-name/<str:name>", TenantByName.as_view()),
    path("tenants/by-apartment/", TenantsByApartment.as_view()), #ex: by-apartment/?apartment__number=101

    #apartment endpoints
    path("apartments/", ApartmentList.as_view()),
    path("apartments/by-number/<str:number>", ApartmentByNumber.as_view()),
    path("apartments/by-date-available/", ApartmentsByAvailableDate.as_view()) # ex: by-date-available/?date_available=2023-06-05
]

urlpatterns = format_suffix_patterns(urlpatterns)