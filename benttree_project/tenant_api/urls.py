from django.urls import path
from .views import TenantList, TenantByName, TenantsByApartment

urlpatterns = [
    path("", TenantList.as_view()),
    path("by-name/<str:name>", TenantByName.as_view()), # ex: by-name/Nathan Fielding
    path("by-apartment/", TenantsByApartment.as_view()) # ex: by-apartment/?apartment_number=601A
]