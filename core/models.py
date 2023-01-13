from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=1000)
    roll = models.IntegerField()
    age = models.IntegerField()
    profile = models.TextField()
    data_enrolled = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

