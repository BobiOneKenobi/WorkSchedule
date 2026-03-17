from django.urls import path
from .views import (
    ShiftListView,
    ShiftDetailView,
    ShiftCreateView,
    ShiftUpdateView,
    ShiftDeleteView,
    LeaveRequestListView,
    LeaveRequestCreateView,
    HolidayListView,
    MorningShiftListView,
    AfternoonShiftListView,
    NightShiftListView
)
urlpatterns = [
    path('shifts/', ShiftListView.as_view(), name='shift-list'),
    path('shifts/create/', ShiftCreateView.as_view(), name='shift-create'),
    path('shifts/<int:pk>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('shifts/<int:pk>/edit/', ShiftUpdateView.as_view(), name='shift-edit'),
    path('shifts/<int:pk>/delete/', ShiftDeleteView.as_view(), name='shift-delete'),
    path('leave/', LeaveRequestListView.as_view(), name='leave-list'),
    path('leave/create/', LeaveRequestCreateView.as_view(), name='leave-create'),
    path('holidays/', HolidayListView.as_view(), name='holiday-list'),
    path('shifts/morning/', MorningShiftListView.as_view(), name='morning-shifts'),
    path('shifts/afternoon/', AfternoonShiftListView.as_view(), name='afternoon-shifts'),
    path('shifts/night/', NightShiftListView.as_view(), name='night-shifts'),
    ]