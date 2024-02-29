from django.core.management.base import BaseCommand
from employeesapp.models import Employee
import random
import datetime

class Command(BaseCommand): #добавление команды, вып-й через консоль
    """
    Creates new  employee
    """
    def handle(self, *args, **options):
        self.stdout.write("Create new employee") #для проверки создания

        employees_names = [
            "Fdfg Rfghfg Eghjghj",
            "Lkjhkj Uhv Tgfhg",
            "Qdfg Tdfg Edfgd",
        ]
        position_names = [
            "sdff",
            "werwerwe",
            "sdfsd",
        ]
        chief_names = [
            "ghghjg sdfsdf",
            "qqwe ytyj",
            "oihio jkjkh iuoip",
        ]

        for employee_name in employees_names:
            year = random.randint(1995, 2024)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            date = datetime.date(year, month, day)
            empl, created = Employee.objects.get_or_create(name=employee_name,
                                                  position=random.choice(position_names),
                                                  date_of_empl=date,
                                                  salary=random.randint(500, 5000),
                                                  chief=random.choice(chief_names))
            self.stdout.write(self.style.SUCCESS(f"Created record {empl.name}"))