from django.db import models

# Create your models here.
class Attending(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.TextField(default='X')
    def __str__(self):
        return f"{self.name}, {self.email}"
    
class Events(models.Model):
    leader_name = models.TextField(max_length=50)
    team_name = models.TextField(max_length=50)
    phone = models.TextField(default='X')
    activity = models.TextField(max_length=50)
