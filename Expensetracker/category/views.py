from django.shortcuts import render
from .models import Category,Adding_Expense_To_Categoory
from django.http import HttpResponse

# Create your views here.
def index(request):
    q=Category.objects.all()
    context={'Category':q}
    return render(request,'category/index.html',context)


def all_expense(request):
    q=Adding_Expense_To_Categoory.objects.all()
    context={'Category':q}
    return render(request,'category/all_expense.html',context)
def add_category(request):
    
    return render(request,'category/add_category.html')

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Category()
                post.title= request.POST.get('title')
                
                post.save()
                
                return render(request, 'posts/create.html')  

        else:
                return render(request,'posts/create.html')


def new_category(request):
    if request.method == 'POST':
        pass
    """
    working on form to get category from ui
    """