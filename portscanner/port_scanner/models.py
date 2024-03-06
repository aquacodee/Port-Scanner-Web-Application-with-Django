from django.db import models


class ScanResult(models.Model):
    ip_address = models.CharField(max_length=100)
    port = models.IntegerField()
    is_open = models.BooleanField(default=False)
    service = models.CharField(default=False, max_length=150)
    vulnerability = models.BooleanField(default=False)
