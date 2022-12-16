from django.db import models

class Apartment(models.Model):
    number = models.CharField(max_length=7)
    property = models.CharField(max_length=25)
    occupants = models.IntegerField()
    date_available = models.DateField(null=True)

    def __str__(self):
        return self.number

class Tenant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default="@gmail.com")
    phone_number = models.CharField(max_length=13, unique=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.PROTECT, null=True)
    is_renewing = models.BooleanField(default=False)
    copy_of_lease = models.FileField(upload_to="leases", null=True)