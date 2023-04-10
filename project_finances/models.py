# project_finances/models.py
from django.db import models
from projects.models import Project

class ProjectFinance(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.project} - Finance"

class FeeProposal(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    proposed_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.project} - Fee Proposal"

class Invoice(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateField()

    def __str__(self):
        return f"{self.project} - Invoice {self.invoice_number}"
