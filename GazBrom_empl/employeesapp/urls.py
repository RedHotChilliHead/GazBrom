from django.urls import path
from .views import employees_list, EmployeeDetailsView, EmployeeUpdateView, EmployeeCreateView, EmployeeDeleteView, \
    EmployeeListView

app_name = "employeesapp"

urlpatterns = [
    path('', employees_list, name='employees_list'),  # к функции можно будет обращаться по name
    path('employees/all/', EmployeeListView.as_view(), name='employees_list_all'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeDetailsView.as_view(), name='employee_details'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]