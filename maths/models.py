from django.db import models

class Math(models.Model):
    operation = models.CharField(max_length=5)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'maths'

class Result(models.Model):  # Dodaj definicję klasy Result
    # Definicja pól dla klasy Result
    pass