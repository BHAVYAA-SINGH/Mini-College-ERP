from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import CourseForm
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def course_list(request):
    courses=Course.objects.all()
    context={
        'courses' : courses,
    }
    return render(request,'courses/course_list.html',context)

@login_required
def course_detail(request,pk):
    course=get_object_or_404(Course,pk=pk)
    context={
        'course':course
    }
    return render(request,'courses/course_detail.html',context)

@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course=form.save(commit=True)
            return redirect('courses:list')
        
    else:
        form=CourseForm()
    context={'form':form,}
    return render(request,'courses/add_course.html',context)
    
@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
        
    context = {'form': form, 'course': course }
    return render(request, 'courses/edit_course.html', context)

@login_required 
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete() 
        return redirect('courses:list')
    context = {'course': course}
    return render(request, 'courses/delete_course.html', context)

