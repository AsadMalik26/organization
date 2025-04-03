from django.urls import path

from employee.views import EmployeeAPIView
from project.views import ProjectAPIView
from team.views import TeamsAPIView

urlpatterns = [
    path('get/<int:id>', TeamsAPIView.as_view(), name='single-team'),
    path('', TeamsAPIView.as_view(), name='team-view'),
]
