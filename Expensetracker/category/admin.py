from django.contrib import admin
from . models import Category,Adding_Expense_To_Categoory,Budget
# Register your models here.
admin.site.register(Category)
admin.site.register(Adding_Expense_To_Categoory)
admin.site.register(Budget)