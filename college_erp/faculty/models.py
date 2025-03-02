from django.db import models

class Faculty(models.Model):
    DESIGNATION_CHOICES = [
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
    ]
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.designation}"
