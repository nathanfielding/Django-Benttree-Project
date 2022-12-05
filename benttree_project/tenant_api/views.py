from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TenantSerializer, AddTenantSerializer
from .models import Tenant

class TenantView(generics.CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class AddTenantView(APIView):
    serializer_class = AddTenantSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"Bad request": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        tenant_name = serializer.data.get("name")
        self.queryset = Tenant.objects.filter(name=tenant_name)
        if self.queryset.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        tenant = Tenant(name=tenant_name, 
                        phone_number=serializer.data.get("phone_number"), 
                        apartment_number=serializer.data.get("apartment_number"), 
                        lease_start=serializer.data.get("lease_start"), 
                        lease_end=serializer.data.get("lease_end"), 
                        is_renewing=serializer.data.get("is_renewing"),
                        copy_of_lease=serializer.data.get("copy_of_lease")
                        )
        tenant.save()
        return Response(TenantSerializer(tenant).data, status=status.HTTP_201_CREATED)