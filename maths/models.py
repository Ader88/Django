from django.db import models

# Create your models here.

class Math(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    operation = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"id:{self.id}, a={self.a}, b={self.b}, op={self.operation}"
    
class Result(models.Model):
    value = models.FloatField()
    error = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'value: {self.value} | error: {self.error}'
