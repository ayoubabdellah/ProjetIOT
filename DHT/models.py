import logging

from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.db import models
class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        try:
            if self.temp is not None and self.temp > 20:
                from DHT.views import sendtele
                sendtele()

                subject = f"Température dépasse la normale: {self.temp}"
                message = f"Anomalie dans la machine le {self.dt}"
                from_email = "ayoubabdellah29@gmail.com"
                recipient_list = ["ayoubabdellah10@gmail.com"]

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return super().save(*args, **kwargs)

        except Exception as e:
            logging.error(f"An error occurred in save method: {e}")