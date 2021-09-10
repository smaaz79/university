from django.db import models
import django.db.models.fields.related

# Create your models here.
class Student(models.Model):
    fname= models.CharField(max_length=25)
    lname= models.CharField(max_length=25)
    address = models.ForeignKey('Address',null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.fname + ',' + self.lname


class Teacher(models.Model):
    name = models.CharField(max_length=25)
    address = models.ForeignKey('Address', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey('Teacher', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.street + ',' + self.city + ',' + self.state