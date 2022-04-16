import imp
from re import T
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Department(models.Model):
    name = models.CharField(_("Department name"), max_length=100)
    manager = models.OneToOneField("Employee", verbose_name=_("Department's Manger"), on_delete=models.CASCADE, related_name='manger', null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    # gender choses
    GENDER_CHOSES = [
        ('m', 'Male'),
        ('f', 'Famale'),
        (None, 'Not known')
        # django direct will choses the none value
        # 
    ]
    id = models.IntegerField(_("Employee's id"), unique=True, primary_key=True)
    name = models.CharField(_("Employee name"), max_length=50)
    gender = models.CharField(_("Employee's gender"), max_length=50, choices=GENDER_CHOSES, blank=True)
    email = models.EmailField(_("employee's email"), max_length=254, blank=True, null=True)
    department = models.ForeignKey("Department", verbose_name=_("Employee department"), on_delete=models.CASCADE)
    join_date = models.DateField(_("Employee's join date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'Employee No.{self.id} - {self.name}'
    