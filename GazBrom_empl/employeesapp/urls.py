from django.urls import path
from .views import employees_list, EmployeeDetailsView, EmployeeUpdateView

app_name = "employeesapp"

urlpatterns = [
    path('', employees_list, name='employees_list'), #к функции можно будет обращаться по name
    path('employees/<int:pk>/', EmployeeDetailsView.as_view(), name='employee_details'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
]