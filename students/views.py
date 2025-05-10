from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required 

# Create your views here.

@login_required
def student_list(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request, 'students/student_list.html',context)

@login_required
def student_detail(request,pk):
    student = get_object_or_404(Student,pk=pk)
    context={'student':student}
    return render(request,'students/student_detail.html',context)

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student=form.save(commit=True)
            return redirect('students:list')
        
    else:
        form=StudentForm()
    context={'form':form,}
    return render(request,'students/add_student.html',context)
    
@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
        
    context = {'form': form, 'student': student }
    return render(request, 'students/edit_student.html', context)

@login_required 
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete() 
        return redirect('students:list')
    context = {'student': student }
    return render(request, 'students/delete_student.html', context)

@login_required
def add_enrollment(request,student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = student
            enrollment.save()
            return redirect('students:detail', pk=student.pk)
    else:
        form = EnrollmentForm()
    context = {
        'form': form,
        'student': student, 
        'adding_for_student': True 
    }
    return render(request, 'students/add_enrollment.html', context)

@login_required
def delete_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    student_pk = enrollment.student.pk
    if request.method == 'POST':
        enrollment.delete()
        return redirect('students:detail', pk=student_pk)
    context = {'enrollment': enrollment} 
    return render(request, 'students/delete_enrollment.html', context)