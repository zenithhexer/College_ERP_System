from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=255)
    enrollment_number = models.CharField(max_length=50, unique=True)
    date_of_admission = models.DateField()
    
    def __str__(self):
        return f"{self.name} - {self.enrollment_number}"