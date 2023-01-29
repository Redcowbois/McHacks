from django.db import models
from django.contrib import admin
# Create your models here.


class User(models.Model): #Class for the user
    name = models.CharField(max_length=200)

    def __str__(self): 
        return str(self.name)

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=200)

class Day(models.Model): 
    user = models.ForeignKey(Friend, on_delete=models.CASCADE)
    day = models.CharField(max_length=200)
    
class Course(models.Model): #Class for each different course 
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def __str__(self): 
        return str(self.course)

class ScheduleImage(models.Model):
   image = models.ImageField(null = True, blank = True, upload_to = "images/") 

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Day)
admin.site.register(Course)
admin.site.register(ScheduleImage)