from django.utils import timezone
from django.utils.timezone import timedelta

from django.db import models

class RegisterForm(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateTimeField()
    payment_method_ic = models.CharField(max_length=30)
    inicial_contributions = models.DecimalField(max_digits=11, decimal_places=2)
    payment_method_is = models.CharField(max_length=30)
    initial_savings = models.DecimalField(max_digits=11, decimal_places=2)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class LoanForm(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateTimeField(null=True)
    cedula = models.CharField(max_length=20)
    loan_amount = models.DecimalField(max_digits=11, decimal_places=2)
    monthly_income = models.DecimalField(max_digits=11, decimal_places=2)
    phone_number = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100 , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
