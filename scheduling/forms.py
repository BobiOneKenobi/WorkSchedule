from django import forms
from .models import Shift, LeaveRequest, Holiday
class BaseShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['employee', 'date', 'start_time', 'end_time', 'shift_type', 'skills_required']
        labels = {'employee': 'Employee','date': 'Shift Date','start_time': 'Start Time','end_time': 'End Time','shift_type': 'Shift Type','skills_required': 'Required Skills',
        }
        help_texts = {'date': 'Select the working date.','skills_required': 'Select one or more skills if needed.',
        }
        widgets = {'date': forms.DateInput(attrs={'type': 'date'}),'start_time': forms.TimeInput(attrs={'type': 'time'}),'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError('End time must be later than start time.')
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