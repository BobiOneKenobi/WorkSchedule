from django.db import models
from django.core.validators import MinLengthValidator

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True,validators=[MinLengthValidator(2)])
    code = models.CharField(max_length=10, unique=True)
    manager_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    class Meta:
        ordering = ['name']
    def __str__(self):
        return f"{self.name} - ({self.code})"
class Employee(models.Model):
    first_name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    job_title = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='employees')
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

