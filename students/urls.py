from django.urls import path
from .import views

app_name = 'students'
urlpatterns = [
    path('',views.student_list,name='list'),
    path('add/', views.add_student, name='add'),
    path('<int:pk>/edit/', views.edit_student, name='edit'),
    path('<int:pk>/delete/', views.delete_student, name='delete'),
    path('<int:student_pk>/enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/<int:pk>/delete/', views.delete_enrollment, name='delete_enrollment'),
    path('<int:pk>/',views.student_detail,name='detail'),

]
