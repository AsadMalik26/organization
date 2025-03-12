from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skill')
    def __str__(self):
        return f"{self.name} ({self.department})"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name_plural = "Skills"
class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Employee)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
