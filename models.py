from django.db import models

# Create your models here.
class DeviceRequest(models.Model):
    d_id = models.AutoField(primary_key=True)
    dev_name = models.CharField(max_length=50)
    request = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'device_request'
