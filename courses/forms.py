from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'credits', 'description']
        labels = {
            'course_code': 'Course Code',
            'course_name': 'Course Name',
            'credits': 'Credits',
            'description': 'Description',
        }