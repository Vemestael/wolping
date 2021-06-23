from django.db import models

# Create your models here.
class Data(models.Model):
    ip_address = models.CharField(max_length=15)
    mac_address = models.CharField(max_length=17)

    def __str__(self) -> str:
        return f"{self.ip_address}\t|\t{self.mac_address}"
