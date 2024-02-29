from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse, HttpRequest

def employees_list(request: HttpRequest):
    context = {
        "employees": Employee.objects.all()
    }
    return render(request, 'employeesapp/employees-list.html', context=context)
