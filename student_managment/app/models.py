from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)


class Course(models.Model):
    Course_Name = models.CharField(max_length=200)
    Fess = models.FloatField()
    Duration = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Course_Name


Gender_choice = (
    ('male', 'male'),
    ('female', 'female'),
)


class AddTeacher(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    JoiningDate = models.DateField()
    Experience = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='teacherimage/')
    Email = models.EmailField()
    Contact = models.CharField(max_length=100)
    Gender = models.CharField(choices=Gender_choice, max_length=100)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    Picture = models.ImageField(upload_to='studentimage/')
    address = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
