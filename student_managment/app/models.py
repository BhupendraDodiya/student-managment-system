from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)

class student_dashboard(models.Model):
    Course_Name = models.CharField(max_length=200)
    Fess = models.FloatField()
    Duration = models.CharField(max_length=100)
    Description = models.TextField()