from django.db import models

# Create your models here.
class Departments(models.model):
	DepartmentId = models.AutoField(primary_key =True)
	DepartmentName = models.CharField(max_length=500)

class Employees(models.model):
	EmployeeId = models.AutoField(primary_key =True)
	EmployeeName = models.CharField(max_length=500)
	Department = models.CharField(max_length=500)
	DateOfJoining = models.CharField(max_length=500)
	PhotoFileName = models.CharField(max_length=500)