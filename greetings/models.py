from django.db import models

class GreetingCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Greeting(models.Model):
    category = models.ForeignKey(GreetingCategory, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message