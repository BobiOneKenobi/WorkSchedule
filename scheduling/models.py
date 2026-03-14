from django.core.validators import  MinLengthValidator
from django.db import models
from django.core.exceptions import ValidationError


class Skill(models.Model):
    name = models.CharField(max_length=50,unique=True,validators=[MinLengthValidator(2)])
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
class Shift(models.Model):
    SHIFT_TYPE = (('morning', 'Morning'),('afternoon','Afternoon'),('night','Night'),)
    employee = models.ForeignKey('employees.Employee',on_delete=models.CASCADE,related_name='shifts')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    shift_type = models.CharField(max_length=20,choices=SHIFT_TYPE)
    skills_required = models.ManyToManyField(Skill,blank=True,related_name='shifts')
    class Meta:
        ordering = ['date','start_time']
    def __str__(self):
        return f"{self.employee} - {self.date} - ({self.start_time})"
    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")
class LeaveRequest(models.Model):
    STATUS_CHOICES = (('pending','Pending'),('approved','Approved'),('rejected','Rejected'),)
    employee = models.ForeignKey('employees.Employee',on_delete=models.CASCADE,related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(validators=[MinLengthValidator(10)])
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    class Meta:
        ordering = ['-start_date']
    def __str__(self):
        return f"{self.employee} - ({self.start_date}) - ({self.end_date})"
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")
class Holiday(models.Model):
    name = models.CharField(max_length=100,unique=True,validators=[MinLengthValidator(2)])
    date = models.DateField(unique=True)
    is_paid = models.BooleanField(default=True)
    class Meta:
        ordering = ['date']
    def __str__(self):
        return f"{self.name} - ({self.date})"

