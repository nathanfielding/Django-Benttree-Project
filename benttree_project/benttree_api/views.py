from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter
from .serializers import TenantSerializer, ApartmentSerializer
from .models import Tenant, Apartment

class TenantList(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantByName(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    #required for when returning a single object of the queryset
    lookup_field = "name"

class TenantsByApartment(generics.ListAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    
    # required for when returning a subset of the queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["apartment_number"]


class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentByNumber(generics.RetrieveDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    lookup_field = "number"


class AvailableDateFilterSet(FilterSet):
    date_available = DateFilter(field_name="date_available", lookup_expr="gte")
    class Meta:
        model = Apartment
        fields = ["date_available"]


class ApartmentsByAvailableDate(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = AvailableDateFilterSet