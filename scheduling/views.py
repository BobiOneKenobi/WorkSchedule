from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import ShiftCreateForm, ShiftEditForm, ShiftDeleteForm
from .models import Shift
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