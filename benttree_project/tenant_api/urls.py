from django.urls import path
from .views import TenantList, TenantByName

urlpatterns = [
    path("", TenantList.as_view()),
    path("by-name/<str:name>", TenantByName.as_view()),
]