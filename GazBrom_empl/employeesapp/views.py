from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import render, reverse
from .models import Employee
from django.http import HttpResponse, HttpRequest
from django.views.generic import UpdateView


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

    return render(request, 'employeesapp/employees-list-2.html', context=context)

class EmployeeDetailsView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        employee = get_object_or_404(Employee, pk=pk)
        context = {
            "Employee": employee,
        }
        return render(request, 'employeesapp/employee-details.html', context=context)

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = "name", "position", "date_of_empl", "salary", "chief", "hierarchy", "photo"
    template_name_suffix = "_update"
    def get_success_url(self): #функция создаем ссылку с атрибутом pk, просто так pk не достать на этом уровне
        return reverse("employeesapp:employee_details", kwargs={"pk": self.object.pk})

    # def post(self, request: HttpRequest, pk: int) -> HttpResponse:
    #     employee = get_object_or_404(Employee, pk=pk)
    #     context = {
    #         "Employee": employee,
    #     }
    #     myfile = request.FILES["myfile"]
    #     fs = FileSystemStorage(location='/media/images')
    #     filename = fs.save(myfile.name, myfile)
    #     print(f"Saved file: {filename}")
    #     employee.photo = fs.url(filename)
    #     # employee.photo.save(myfile.name, myfile)
    #     return render(request, 'employeesapp/employee-details.html', context=context)
