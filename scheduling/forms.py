from django import forms
from .models import Shift, LeaveRequest
from datetime import  datetime, timedelta
class BaseShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['employee', 'date', 'start_time', 'end_time', 'skills_required']
        labels = {
            'employee': 'Employee',
            'date': 'Shift Date',
            'start_time': 'Start Time',
            'end_time': 'End Time',
            'skills_required': 'Required Skills',
        }
        help_texts = {'date': 'Select the working date.',
            'start_time': 'Shift type is assigned automatically based on the start time.',
            'skills_required': 'Select one or more skills if needed.',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        shift_date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if employee and shift_date and start_time and end_time:
            if start_time == end_time:
                raise forms.ValidationError('Start time and end time cannot be the same.')

            start_dt = datetime.combine(shift_date, start_time)
            end_dt = datetime.combine(shift_date, end_time)

            if end_dt <= start_dt:
                end_dt += timedelta(days=1)

            duration = end_dt - start_dt

            if duration > timedelta(hours=12):
                raise forms.ValidationError('Shift duration cannot be longer than 12 hours.')

            existing_shifts = Shift.objects.filter(employee=employee)

            if self.instance.pk:
                existing_shifts = existing_shifts.exclude(pk=self.instance.pk)

            for existing_shift in existing_shifts:
                existing_start = datetime.combine(existing_shift.date, existing_shift.start_time)
                existing_end = datetime.combine(existing_shift.date, existing_shift.end_time)

                if existing_end <= existing_start:
                    existing_end += timedelta(days=1)

                overlaps = start_dt < existing_end and end_dt > existing_start

                if overlaps:
                    raise forms.ValidationError(
                        'This employee already has an overlapping shift for the selected time period.'
                    )
        return cleaned_data
class ShiftCreateForm(BaseShiftForm):
    pass
class ShiftEditForm(BaseShiftForm):
    pass
class ShiftDeleteForm(BaseShiftForm):
    class Meta(BaseShiftForm.Meta):
        fields = ['employee', 'date', 'start_time', 'end_time', 'shift_type', 'skills_required']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.disabled = True
    def clean(self):
        return self.cleaned_data
class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'start_date', 'end_date', 'reason']
        labels = {
            'employee': 'Employee',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'reason': 'Reason',
        }
        help_texts = {
            'reason': 'Explain the leave request briefly.',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter leave reason'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError('End date cannot be earlier than start date.')
        if employee and start_date and end_date:
            overlapping_requests = LeaveRequest.objects.filter(
                employee=employee,
                start_date__lte=end_date,
                end_date__gte=start_date,
            ).exclude(status='rejected')
            if self.instance.pk:
                overlapping_requests = overlapping_requests.exclude(pk=self.instance.pk)
            if overlapping_requests.exists():
                raise forms.ValidationError(
                    'This employee already has a leave request for the selected period.'
                )
        return cleaned_data