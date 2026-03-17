from django.contrib import admin
from .models import Skill, Shift, LeaveRequest, Holiday

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'start_time', 'end_time', 'shift_type')
    search_fields = ('employee__first_name', 'employee__last_name', 'shift_type')
    list_filter = ('date', 'shift_type', 'skills_required')
    ordering = ('date', 'start_time')
    filter_horizontal = ('skills_required',)


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status', 'duration_days')
    search_fields = ('employee__first_name', 'employee__last_name', 'reason')
    list_filter = ('status', 'start_date', 'end_date')
    ordering = ('-start_date',)
    actions = ['mark_as_approved', 'mark_as_rejected']

    @admin.action(description='Mark selected leave requests as approved')
    def mark_as_approved(self, request, queryset):
        queryset.update(status='approved')

    @admin.action(description='Mark selected leave requests as rejected')
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='rejected')


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'is_paid')
    search_fields = ('name',)
    list_filter = ('is_paid', 'date')
    ordering = ('date',)
