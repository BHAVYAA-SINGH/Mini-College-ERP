from django.db import models

# Create your models here.
class Course(models.Model):
    course_code=models.CharField(max_length=10,unique=True)
    course_name=models.CharField(max_length=200)
    credits=models.IntegerField()
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.course_code}: {self.course_name}"