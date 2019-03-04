from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Bill(models.Model):
    service = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    dueDate = models.DateTimeField(default=timezone.now)
    payedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.service