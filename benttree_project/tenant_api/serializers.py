from rest_framework import serializers
from .models import Tenant, Apartment

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ["id", "name", "email", "phone_number", "apartment", "is_renewing", "copy_of_lease"]

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ["number", "property", "occupants", "date_available"]