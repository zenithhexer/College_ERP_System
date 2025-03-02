from django.db import models

# Create your models here.
class Administrator(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.role}"