# Generated by Django 4.0.3 on 2022-04-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_alter_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Famale'), (None, 'Not known')], default='---------', max_length=50, verbose_name="Employee's gender"),
        ),
    ]
