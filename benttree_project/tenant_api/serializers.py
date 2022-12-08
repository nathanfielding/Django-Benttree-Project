from rest_framework import serializers
from .models import Tenant

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ("id", "name", "phone_number", "apartment_number", "lease_start", "lease_end", "is_renewing", "copy_of_lease")