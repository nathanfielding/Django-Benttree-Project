from django.urls import path
from .views import TenantView, AddTenantView

urlpatterns = [
    path("", TenantView.as_view()),
    path("add-tenant", AddTenantView.as_view())
]