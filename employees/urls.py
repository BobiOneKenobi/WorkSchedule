from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)
urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),]