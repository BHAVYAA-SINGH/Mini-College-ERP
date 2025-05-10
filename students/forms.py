from django import forms
from .models import *
from courses.models import Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'email', 'date_of_enrollment']
        labels = {
            'student_id': 'Student ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'date_of_enrollment': 'Date of Enrollment',
        }

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        exclude = ['student', 'enrollment_date']
        labels = {
            'course': 'Course',
            'grade': 'Grade',
        }