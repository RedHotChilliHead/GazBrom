# Generated by Django 5.0.2 on 2024-02-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hierarchy',
            field=models.IntegerField(default=6),
        ),
    ]
