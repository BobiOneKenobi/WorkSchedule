from django import forms
from .models import Employee
class BaseEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title', 'email', 'hire_date', 'department']
        labels = {'first_name': 'First Name','last_name': 'Last Name','job_title': 'Job Title','email': 'Email Address',
                  'hire_date': 'Hire Date','department': 'Department',
        }
        help_texts = {'email': 'Enter a valid company email address.','hire_date': 'Select the employee hire date.',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Enter job title'}),'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.strip()
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.strip()
    def clean_job_title(self):
        job_title = self.cleaned_data['job_title']
        return job_title.strip()
class EmployeeCreateForm(BaseEmployeeForm):
    pass
class EmployeeEditForm(BaseEmployeeForm):
    pass
class EmployeeDeleteForm(BaseEmployeeForm):
    class Meta(BaseEmployeeForm.Meta):
        fields = ['first_name', 'last_name', 'job_title', 'email', 'hire_date', 'department']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.disabled = True
    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance