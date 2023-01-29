from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model): #Class for the user
    name = models.CharField(max_length=200)

    def __str__(self): 
        return str(self.name)

class Day(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=200)
    
class Course(models.Model): #Class for each different course 
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def __str__(self): 
        return str(self.course)