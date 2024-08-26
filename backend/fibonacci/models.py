from django.db import models

# Create your models here.
class FibonacciData(models.Model):
    value = models.IntegerField()
    serie = models.JSONField()

    def __str__(self):
        return f"Value: {self.value}, Series: {self.serie}"