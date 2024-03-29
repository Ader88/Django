from django.db import models

class Math(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    operation = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    result = models.IntegerField(null=True, default=None)

    def __str__(self):
        return f"id:{self.id}, a={self.a}, b={self.b}, op={self.operation}, result={self.result}"
    
class Result(models.Model):
    value = models.FloatField(null=True, blank=True)
    error = models.CharField(max_length=255, default='Error')

    def __str__(self):
        return f'value: {self.value} | error: {self.error}'