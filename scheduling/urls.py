from django.urls import path
from .views import (
    ShiftListView,
    ShiftDetailView,
    ShiftCreateView,
    ShiftUpdateView,
    ShiftDeleteView,
)
urlpatterns = [
    path('shifts/', ShiftListView.as_view(), name='shift-list'),
    path('shifts/create/', ShiftCreateView.as_view(), name='shift-create'),
    path('shifts/<int:pk>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('shifts/<int:pk>/edit/', ShiftUpdateView.as_view(), name='shift-edit'),
    path('shifts/<int:pk>/delete/', ShiftDeleteView.as_view(), name='shift-delete'),
    ]