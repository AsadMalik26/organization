from django.urls import path

from employee.views import EmployeeAPIView

urlpatterns = [
    path('get/<int:id>', EmployeeAPIView.as_view(), name='single-employee'),
    path('', EmployeeAPIView.as_view(), name='employee-view'),
]
