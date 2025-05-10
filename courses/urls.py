from django.urls import path
from . import views

app_name='courses'

urlpatterns = [
    path('',views.course_list,name='list'),path('add/', views.add_course, name='add'),
    path('<int:pk>/edit/', views.edit_course, name='edit'),
    path('<int:pk>/delete/', views.delete_course, name='delete'),
    path('<int:pk>',views.course_detail,name='detail'),
]