
from django.contrib import admin
from django.urls import path, include

from basicorg.views import EmployeeView, DepartmentView, ProjectView, SkillView, TeamView

urlpatterns = [
    path('departments/', DepartmentView.as_view(), name='department'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('project/', ProjectView.as_view(), name='project'),
    path('skill/', SkillView.as_view(), name='skill'),
    path('team/', TeamView.as_view(), name='team'),
]
