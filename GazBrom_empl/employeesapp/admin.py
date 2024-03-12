from django.contrib import admin
from employeesapp.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'position', 'date_of_empl', 'salary', 'chief', 'hierarchy'
    list_display_links = "pk", "name"
    ordering = ('hierarchy',)
    search_fields = ('pk', 'name', 'position', 'date_of_empl', 'salary', 'chief', 'hierarchy')

# Register your models here.
