from django.core.management.base import BaseCommand
from employeesapp.models import Employee


class Command(BaseCommand):
    """
    Delete some  employees
    """

    def handle(self, *args, **options):
        self.stdout.write("Delete all employees")

        Employee.objects.all().delete()
