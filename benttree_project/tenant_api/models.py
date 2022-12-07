from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

class Tenant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    apartment_number = models.CharField(max_length=10)
    lease_start = models.DateField()
    lease_end = models.DateField()
    is_renewing = models.BooleanField(default=False)
    copy_of_lease = models.FileField(upload_to="leases")
