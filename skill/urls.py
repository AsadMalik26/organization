from django.contrib import admin
from django.urls import path, include

from department.views import DepartmentListAPIView, DepartmentCreateAPIView, DepartmentListArnonAPIView, \
    DepartmentCreateWithModelView, DepartmentCreateWithSerializerView, DepartmentGetAPIView, DepartmentUpdateAPIView, \
    DepartmentDeleteAPIView
from skill.views import SkillsAPIView

urlpatterns = [
    path('get/<int:id>', SkillsAPIView.as_view(), name='single-skill'),
    path('', SkillsAPIView.as_view(), name='skill-view'),
]
