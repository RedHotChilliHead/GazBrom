from django.urls import path
from .views import employees_list

app_name = "employeesapp"

urlpatterns = [
    path('', employees_list, name='employees_list'), #к функции можно будет обращаться по name
]