# payrolls/models.py
from django.db import models
from projects.models import Project
from accounts.models import UserProfile

class Payroll(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user} - {self.project} - {self.period_start} - {self.period_end}"

