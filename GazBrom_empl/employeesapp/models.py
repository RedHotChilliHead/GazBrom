from django.db import models

class Employee(models.Model):
    # class Meta: #конфигурационный класс
    #     ordering = ["name", "price"] #сортировка по полю по алфавиту
    #     db_table = "tech_products" через какую таблицу запрашивать данные
    #     verbose_name_plural = "products" объявлять в множ. числе
    name = models.CharField(max_length=150)
    position = models.TextField(null=False, blank=True)
    date_of_empl = models.DateTimeField(null=False, blank=True)
    salary = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    chief = models.CharField(max_length=150)
    hierarchy = models.IntegerField(default=6, null=False)
