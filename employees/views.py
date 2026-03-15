from .forms import EmployeeCreateForm, EmployeeEditForm
from .models import Employee
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee-list.html'
    context_object_name = 'employees'
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee-detail.html'
    context_object_name = 'employee'
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employees/employee-create.html'
    success_url = reverse_lazy('employee-list')
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeEditForm
    template_name = 'employees/employee-edit.html'
    success_url = reverse_lazy('employee-list')
class EmployeeDeleteView(View):
    template_name = 'employees/employee-delete.html'
    success_url = reverse_lazy('employee-list')
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            'employee': employee
        }
        return render(request, self.template_name, context)
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect(self.success_url)