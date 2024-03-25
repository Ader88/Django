from django.db import models

class Math(models.Model):
    operation = models.CharField(max_length=5)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'maths'

class Result(models.Model):
    value = models.FloatField(null=True)
    error = models.CharField(max_length=255, null=True)

    class Meta:
        app_label = 'maths'
