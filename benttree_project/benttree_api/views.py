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


# class LeaseEndFilterSet(FilterSet):
#     lease_end = DateFilter(field_name="lease_end", lookup_expr="gt")
#     class Meta:
#         model = Tenant
#         fields = ["lease_end"]


# class TenantsByLeaseEnd(generics.ListAPIView):
#     queryset = Tenant.objects.filter(is_renewing=False)
#     serializer_class = TenantSerializer

#     filter_backends = [DjangoFilterBackend]
#     filterset_class = LeaseEndFilterSet