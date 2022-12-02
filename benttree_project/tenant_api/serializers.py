from rest_framework import serializers
from .models import Tenant

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ("id", "name", "phone_number", "apartment_number", "lease_start", "lease_end", "copy_of_lease")

class AddTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ("name", "phone_number", "apartment_number", "lease_start", "lease_end", "copy_of_lease")