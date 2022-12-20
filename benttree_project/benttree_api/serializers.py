from rest_framework import serializers
from .models import Tenant, Apartment

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ["id", "number", "property", "occupants", "date_available"]

class TenantSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer(read_only=True)
    class Meta:
        model = Tenant
        fields = ["id", "name", "email", "phone_number", "apartment", "is_renewing", "copy_of_lease"]