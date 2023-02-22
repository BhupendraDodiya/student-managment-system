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

class AddStudents(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    course = models.ForeignKey(student_dashboard, on_delete=models.CASCADE)