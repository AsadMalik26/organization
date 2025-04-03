from django.urls import path

from employee.views import EmployeeAPIView
from project.views import ProjectAPIView

urlpatterns = [
    path('get/<int:id>', ProjectAPIView.as_view(), name='single-project'),
    path('', ProjectAPIView.as_view(), name='project-view'),
]
