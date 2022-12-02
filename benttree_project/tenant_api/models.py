from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=11)
    apartment_number = models.CharField(max_length=50)
    lease_start = models.DateField()
    lease_end = models.DateField()
    copy_of_lease = models.FileField(upload_to="leases")
