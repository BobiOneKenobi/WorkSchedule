from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'manager_name')
    search_fields = ('name', 'code', 'manager_name')
    ordering = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job_title', 'email', 'hire_date', 'department')
    search_fields = ('first_name', 'last_name', 'email', 'job_title')
    list_filter = ('department', 'hire_date')
    ordering = ('last_name', 'first_name')