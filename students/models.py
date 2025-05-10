from django.db import models
from courses.models import Course
# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True,null=True)
    date_of_enrollment = models.DateField()

    def __str__(self):
        return f"{self.student_id}:{self.first_name} {self.last_name}"
    
class Enrollment(models.Model):
    student=models.ForeignKey('Student',on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date=models.DateField(auto_now_add=True)
    GRADES = [
         ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
        ('W', 'Withdrawal'),
    ]
    grade=models.CharField(max_length=1,choices=GRADES,blank=True,null=True)
    class Meta:
        unique_together=('student','course')
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} enrolled in {self.course.course_code}"

