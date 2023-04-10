# timesheets/models.py
from django.db import models
from projects.models import Project
from accounts.models import UserProfile

class Timesheet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.project} - {self.date}"

