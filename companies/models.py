# companies/models.py
from django.db import models
from accounts.models import UserProfile

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    users = models.ManyToManyField(UserProfile, through='CompanyRole')

    def __str__(self):
        return self.name

class CompanyRole(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} - {self.company} - {self.role}"
