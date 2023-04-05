from django.urls import path
from .views import StudentList, StudentDetails, StudentListCreateView, GraduatingStudentView

urlpatterns=[
    path('students/', StudentList.as_view(),name='student_list'),
    path('student_list/', GraduatingStudentView.as_view(), name='student'),
    path('studentlist/', StudentListCreateView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetails.as_view(), name='StudentDetails')
]