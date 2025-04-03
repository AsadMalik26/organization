from django.shortcuts import render
from rest_framework import viewsets, generics

# from basicorg.models import Employee, Department, Skill, Team, Project

from department.models import Department
from department.serializers import DepartmentSerializer
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from project.models import Project
from project.serializers import ProjectSerializer
from skill.models import Skill
from skill.serializers import SkillSerializer
from team.models import Team
from team.serializers import TeamSerializer


# Create your views here.
class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SkillView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class TeamView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

