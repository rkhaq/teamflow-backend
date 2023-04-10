# projects/models.py
from django.db import models
from companies.models import Company
from accounts.models import UserProfile

class Project(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    users = models.ManyToManyField(UserProfile, through='ProjectRole')

    def __str__(self):
        return self.name

class ProjectRole(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.project} - {self.role}"
