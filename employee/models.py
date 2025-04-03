from django.db import models

from department.models import Department
from skill.models import Skill


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return f"{self.name} ({self.department})"