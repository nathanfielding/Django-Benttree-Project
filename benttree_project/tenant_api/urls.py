from django.urls import path
from .views import TenantList, TenantByName, TenantsByApartment

urlpatterns = [
    path("", TenantList.as_view()),
    path("by-name/<str:name>", TenantByName.as_view()),
    path("by-apartment/<str:apartment_number>", TenantsByApartment.as_view())
]