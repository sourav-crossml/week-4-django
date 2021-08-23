from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    # adding_date = models.DateTimeField()
    def __str__(self) -> str:
        return self.name

class Adding_Expense_To_Categoory(models.Model):
    name=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.IntegerField()
    Discription=models.TextField()
    def __str__(self):
        return self.name

class Budget(models.Model):
    monthly_budget=models.IntegerField()
