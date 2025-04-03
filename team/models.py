from django.db import models

from employee.models import Employee
from project.models import Project


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Employee)
    # project = models.ForeignKey('Project', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name