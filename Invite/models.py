from django.db import models

# Create your models here.
class Attending(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.TextField(default='X')
    def __str__(self):
        return f"{self.name}, {self.email}"
