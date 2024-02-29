from django.core.management.base import BaseCommand
from employeesapp.models import Employee
import random
import datetime


def random_date():
    year = random.randint(1995, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)
    return date


class Command(BaseCommand):  # добавление команды, вып-й через консоль
    """
    Creates new  employee
    """

    def handle(self, *args, **options):
        self.stdout.write("Create new employee")  # для проверки создания

        first_names = ["Oliver", "Jack", "Charlie", "Harry", "Oscar", "Thomas", "Jacob",
                       "Ethan", "William", "Joshua", "Emma", "Olivia", "Sophia", "Isabella",
                       "Ava", "Mia", "Emily", "Abigail", "Madison", "Charlotte"]
        last_names = ["Audley", "Berrington", "Boolman", "Carey", "Donovan", "Finch", "Gibbs",
                      "Haig", "Harrison", "Hawkins", "Finch", "Davidson"]

        position_names1 = ["Сhief executive officer"]
        position_names2 = ["Сhief financial officer", "Chief executive officer",
                           "Financial director, Managing director", "Marketing director",
                           "Human resources director"]
        position_names3 = ["Deputy director"]
        position_names4 = ["Production manager", "Project manager"]
        position_names5 = ["Assistant manager", "Administrative assistant", "Software engineer",
                           "Sales manager", "Recruitment manager", "Legal counsel",
                           "Business development manager", "Customer service manager",
                           "Talent acquisition manager"]

        # генеральный директор
        name = random.choice(first_names) + " " + random.choice(last_names)
        empl, created = Employee.objects.get_or_create(name=name,
                                                       position=random.choice(position_names1),
                                                       date_of_empl=random_date(),
                                                       salary=random.uniform(10000, 15000),
                                                       chief="-",
                                                       hierarchy=1)
        # сотрудники 2 уровня
        eall = Employee.objects.all()
        for position_name in position_names2:
            name = random.choice(first_names) + " " + random.choice(last_names)
            for e in eall:
                if e.position in position_names1:
                    chief2 = e.name
                    break
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=position_name,
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(5000, 10000),
                                                           chief=chief2,
                                                           hierarchy=2)
        # сотрудники 3 уровня
        eall = Employee.objects.all()
        for position_name in position_names2:
            name = random.choice(first_names) + " " + random.choice(last_names)
            for e in eall:
                if e.position == position_name:
                    chief3 = e.name
                    break
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names3),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(3000, 5000),
                                                           chief=chief3,
                                                           hierarchy=3)

        # сотрудники 4 уровня
        eall = Employee.objects.all()
        for i in range(3):
            name = random.choice(first_names) + " " + random.choice(last_names)
            for e in eall:
                if e.position in position_names3:
                    chief4 = e.name
                    break
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names4),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(2000, 3000),
                                                           chief=chief4,
                                                           hierarchy=4)

        # сотрудники 5 уровня
        eall = Employee.objects.all()
        for i in range(5):
            name = random.choice(first_names) + " " + random.choice(last_names)
            for e in eall:
                if e.position in position_names4:
                    chief5 = e.name
                    break
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names5),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(1000, 2000),
                                                           chief=chief5,
                                                           hierarchy=5)
