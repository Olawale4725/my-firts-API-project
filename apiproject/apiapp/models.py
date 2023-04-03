from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'female')
    )
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Male')
    email = models.EmailField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    adress = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.firstname}  - {self.lastname}"
