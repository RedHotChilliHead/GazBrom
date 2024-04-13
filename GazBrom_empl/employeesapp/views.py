from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, reverse
from .models import Employee
from django.http import HttpResponse, HttpRequest
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from django.db.models import Q
from django.core.paginator import Paginator


def employees_list(request: HttpRequest):
    context = {
        "employees1": [],
        "employees2": [],
        "employees3": [],
        "employees4": [],
        "employees5": [],
    }

    eee = Employee.objects.defer('date_of_empl', 'salary').all()
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

class EmployeeListView(LoginRequiredMixin, ListView):
    """
    Отображение Employee без древовидной структуры.
    """
    model = Employee
    context_object_name = "employees"
    paginate_by = 10
    # template_name = 'employeesapp/employee_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'name':
            order_by_field = 'name'
        elif sort_by == 'position':
            order_by_field = 'position'
        elif sort_by == 'date_of_empl':
            order_by_field = 'date_of_empl'
        elif sort_by == 'salary':
            order_by_field = 'salary'
        elif sort_by == 'chief':
            order_by_field = 'chief'
        else:
            order_by_field = 'id'  # По умолчанию сортируем по id

        if query:
            queryset = Employee.objects.defer('hierarchy').filter(
                Q(name__iregex=query) | Q(position__iregex=query) | Q(date_of_empl__iregex=query) |
                Q(salary__iregex=query) | Q(chief__iregex=query) | Q(id__iregex=query)
            )
        else:
            queryset = Employee.objects.defer('hierarchy').all()

        return queryset.order_by(order_by_field)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        context['sort_by'] = self.request.GET.get('sort_by')
        return context

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

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = "name", "position", "date_of_empl", "salary", "chief", "hierarchy", "photo"
    success_url = reverse_lazy("employeesapp:employees_list")  # ссылка на которую перейти после успешного создания сотрудника
    # шаблон должен быть обязательно называться employee_form (employee_form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy("employeesapp:employees_list")
    # шаблон должен быть обязательно employee_confirm_delete (модель_confirm_delete)
