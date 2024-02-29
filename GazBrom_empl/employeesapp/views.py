from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse, HttpRequest

def employees_list(request: HttpRequest):
    context = {
        "employees1": [],
        "employees2": [],
        "employees3": [],
        "employees4": [],
        "employees5": [],
    }

    eee = Employee.objects.all()
    for e in eee:
        if e.hierarchy == 1:
            context["employees1"] += [e]
        elif e.hierarchy == 2:
            context["employees2"] += [e]
        elif e.hierarchy == 3:
            context["employees3"] += [e]
        elif e.hierarchy == 4:
            context["employees4"] += [e]
        elif e.hierarchy == 5:
            context["employees5"] += [e]

    return render(request, 'employeesapp/employees-list.html', context=context)
