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
                       "Ava", "Mia", "Emily", "Abigail", "Madison", "Charlotte", "Aaron", "Abraham",
                       "Adam", "Adrian", "Aidan", "Alan", "Albert", "Alejandro", "Alex", "Alexander",
                       "Alfred", "Andrew", "Angel", "Anthony", "Antonio", "Ashton", "Austin", "Eleanor",
                       "Elizabeth", "Ella", "Erin", "Evelyn", "Jackson", "Jacob", "Jaden", "Jake", "James",
                       "Jason", "Jayden", "Jeffery", "Jeremiah", "Jesse", "Jesus", "John", "Jonathan",
                       "Jordan", "Jose", "Joseph", "Joshua", "Juan", "Julian", "Justin"]
        last_names = ["Audley", "Berrington", "Boolman", "Carey", "Donovan", "Finch", "Gibbs",
                      "Haig", "Harrison", "Hawkins", "Finch", "Davidson", "Attwood", "Audley", "Bates", "Benson",
                      "Barlow", "Bott",
                      "Brickman", "Brown", "Chandler", "Chapman", "Cloud", "Cowell", "Crocket",
                      "Dean", "Dodson", "Duncan", "Evans", "Fletcher", "Foster", "Gates", "Gill", "Green", "Hawkins",
                      "Johnson",
                      "Kirk", "Leman", "Larkins", "Mason", "Miln", "Moor", "Neville", "Osborn", "Palmer", "Pearcy",
                      "Porter",
                      "Rose", "Saunders", "Sheldon", "Sherlock", "Sykes", "Tracy", "Vance", "Ward", "Webster", "Wilson",
                      "White", "Wood", "Young"]

        position_names1 = ["Сhief executive officer"]
        position_names2 = ["Сhief financial officer", "Chief executive officer",
                           "Financial director, Managing director", "Marketing director", "Chief administrative officer"
                           "Human resources director", "The chief economist", "The chief engineer", "The chief accountant",
                           "Chief customer service officer", "Chief technical officer",
                           "Chief safety officer", "Chief purchasing officer", "Chief public relations officer"]
        position_names3 = ["Deputy director", "Budget director", "Art director", "Audit director", "Insurance director",
                           "Marketing Director", "HR Director", "Managing Director"]
        position_names4 = ["Production manager", "Project manager", "Development manager", "HR manager",
                           "Senior manager", "Product manager", "Branch manager", "Project manager",
                           "Tourism manager", "Senior Specialist", "IT Specialist", "Procurement specialist",
                           "Real Estate Specialist"]
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
        # сотрудники 2 уровня (создаем по очереди сотрудника каждой должности второй иерархии)
        ceo = Employee.objects.get(hierarchy=1)
        for position_name in position_names2:
            name = random.choice(first_names) + " " + random.choice(last_names)
            chief = ceo.name
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=position_name,
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(5000, 10000),
                                                           chief=chief,
                                                           hierarchy=2)
        # сотрудники 3 уровня (создаем по очереди подчиненного каждой должности второй иерархии)
        e2pos = Employee.objects.filter(hierarchy=2)
        for e in e2pos:
            name = random.choice(first_names) + " " + random.choice(last_names)
            chief = e.name
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names3),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(3000, 5000),
                                                           chief=chief,
                                                           hierarchy=3)

        # сотрудники 4 уровня (создаем 50 сотрудников 4 иерархии)
        e3pos = Employee.objects.filter(hierarchy=3)
        for i in range(50):
            name = random.choice(first_names) + " " + random.choice(last_names)
            chief4 = random.choice(e3pos).name
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names4),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(2000, 3000),
                                                           chief=chief4,
                                                           hierarchy=4)

        # сотрудники 5 уровня (создаем 100 сотрудников 5 иерархии)
        e4pos = Employee.objects.filter(hierarchy=4)
        for i in range(100):
            name = random.choice(first_names) + " " + random.choice(last_names)
            chief5 = random.choice(e4pos).name
            empl, created = Employee.objects.get_or_create(name=name,
                                                           position=random.choice(position_names5),
                                                           date_of_empl=random_date(),
                                                           salary=random.uniform(1000, 2000),
                                                           chief=chief5,
                                                           hierarchy=5)
