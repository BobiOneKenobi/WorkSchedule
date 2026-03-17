from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import ShiftCreateForm, ShiftEditForm, ShiftDeleteForm, LeaveRequestForm
from .models import Shift,LeaveRequest,Holiday
class ShiftListView(ListView):
    model = Shift
    template_name = 'scheduling/shift-list.html'
    context_object_name = 'shifts'
class ShiftDetailView(DetailView):
    model = Shift
    template_name = 'scheduling/shift-detail.html'
    context_object_name = 'shift'
class ShiftCreateView(CreateView):
    model = Shift
    form_class = ShiftCreateForm
    template_name = 'scheduling/shift-create.html'
    success_url = reverse_lazy('shift-list')
class ShiftUpdateView(UpdateView):
    model = Shift
    form_class = ShiftEditForm
    template_name = 'scheduling/shift-edit.html'
    success_url = reverse_lazy('shift-list')
class ShiftDeleteView(View):
    template_name = 'scheduling/shift-delete.html'
    success_url = reverse_lazy('shift-list')
    def get(self, request, pk):
        shift = get_object_or_404(Shift, pk=pk)
        form = ShiftDeleteForm(instance=shift)
        context = {
            'shift': shift,
            'form': form,
        }
        return render(request, self.template_name, context)
    def post(self, request, pk):
        shift = get_object_or_404(Shift, pk=pk)
        shift.delete()
        return redirect(self.success_url)
class LeaveRequestListView(ListView):
    model = LeaveRequest
    template_name = 'scheduling/leave-list.html'
    context_object_name = 'leave_requests'
class LeaveRequestCreateView(CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'scheduling/leave-create.html'
    success_url = reverse_lazy('leave-list')

    def form_valid(self, form):
        form.instance.status = 'pending'
        return super().form_valid(form)
class HolidayListView(ListView):
    model = Holiday
    template_name = 'scheduling/holiday-list.html'
    context_object_name = 'holidays'
class MorningShiftListView(ListView):
    model = Shift
    template_name = 'scheduling/morning-shifts.html'
    context_object_name = 'shifts'

    def get_queryset(self):
        return Shift.objects.filter(shift_type='morning').order_by('date', 'start_time')
class AfternoonShiftListView(ListView):
    model = Shift
    template_name = 'scheduling/afternoon-shifts.html'
    context_object_name = 'shifts'

    def get_queryset(self):
        return Shift.objects.filter(shift_type='afternoon').order_by('date', 'start_time')
class NightShiftListView(ListView):
    model = Shift
    template_name = 'scheduling/night-shifts.html'
    context_object_name = 'shifts'

    def get_queryset(self):
        return Shift.objects.filter(shift_type='night').order_by('date', 'start_time')