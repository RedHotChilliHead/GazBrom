# Generated by Django 5.0.2 on 2024-03-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeesapp', '0003_alter_employee_options_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
